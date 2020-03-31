# Requirement: pip install ledgerblue
from ledgerblue.comm import getDongle
import struct

TTC_DERIVATION_PATH_PREFIX = "44'/718'/%d'/0/0"


class LedgerAccount:
    def __init__(self):
        self.dongle = getDongle(debug=False)

    def _parse_bip32_path(self, offset):
        path = TTC_DERIVATION_PATH_PREFIX %(offset)
        result = bytes()
        elements = path.split('/')
        for pathElement in elements:
            element = pathElement.split("'")
            if len(element) == 1:
                result = result + struct.pack(">I", int(element[0]))
            else:
                result = result + struct.pack(">I", 0x80000000 | int(element[0]))
        return result

    def get_address(self, offset):
        """
        Query the ledger device for a public ttc address.
        Offset is the number in the HD wallet tree
        """
        donglePath = self._parse_bip32_path(offset)

        apdu =  bytes.fromhex('e0020000') 
        apdu += bytes([len(donglePath) + 1])
        apdu += bytes([len(donglePath) // 4])
        apdu += donglePath

        result = self.dongle.exchange(apdu, timeout=60)


        # Parse result
        offset = 1 + result[0]

        address = result[offset + 1 : offset + 1 + result[offset]]

        return f't0{address.decode()}'

    def get_offset(self, address):
        """
        Convert an address to the HD wallet tree offset
        """
        offset = 0
        while address != self.get_address(offset):
            offset += 1

        return offset


    def list(self, limit=5, page=0):
        """
        List TTC HD wallet adrress of the ledger device
        """
        return list(map(lambda offset: self.get_address(offset), range(page*limit, (page+1)*limit)))

    def sign(self, rlp_encoded_tx, offset=None, address=''):
        """
        Sign an RLP encoded transaction
        """
        if offset is None:
            # Convert an address to an offset
            if address == '':
                raise Exception('Invalid offset and address provided')
            else:
                #TODO check address validity
                offset = self.get_offset(address)

        donglePath = self._parse_bip32_path(offset)

        apdu =  bytes.fromhex('e0040000') 
        apdu += bytes([len(donglePath) + 1 + len(rlp_encoded_tx)])
        apdu += bytes([len(donglePath) // 4])
        apdu += donglePath
        apdu += rlp_encoded_tx

        # Sign with dongle
        result = self.dongle.exchange(apdu, timeout=60)

        # Retrieve VRS from sig
        v = result[0]
        r = int.from_bytes(result[1:1 + 32], 'big')
        s = int.from_bytes(result[1 + 32: 1 + 32 + 32], 'big')

        return (v, r, s)

    def signTx(self, txData):
        pass





