# MARO wallet application for the Ledger Nano S

## Introduction
This is the app for the [Ledger Nano S](https://www.ledgerwallet.com/products/ledger-nano-s) that makes it possible sign any transaction for the maro network.
the tansaction that can be signed include maro transfer , erc20 token transfer and other contract transaction, especially,they also can sign vote transaction that special function in maro network

A companion [Javascript library](https://github.com/LedgerHQ/ledgerjs) is available to communicate with this app.

## Building and installing

To build and install the app on your Nano S or Blue you must set up the Ledger Nano S or Blue build environments. Please follow the Getting Started instructions at the [Ledger Nano S github repository](https://github.com/LedgerHQ/ledger-nano-s).

Alternatively, you can set up the Vagrant Virtualbox Ledger environment maintained [here](https://github.com/fix/ledger-vagrant). This sets up an Ubuntu virtual machine with the Ledger build environment already set up.

apart from this, you can build the Ledger environment by yourself [here](https://ledger.readthedocs.io/en/latest/)

The command to compile and load the app onto the device is:

```$ make load```

To remove the app from the device do:

```$ make delete```


## Test
you can test by python module ledgerblue, but you need to modify the path in ledger.py 
```$ "44'/718'/%d'/0/0"```


### Parsing
When a transaction is to be signed it is sent to the device as a serialized binary object. To show the transaction details to the user on the device this binary object must be read. This is done by a purpose-built parser shipped with this app.

Due to memory limitations the transaction maximum size is set to 1kb. This should be sufficient for most usages, including multi-operation transactions up to 15 operations depending on the size of the operations.

Alternatively the user can enable hash signing. In this mode the parsed transaction is not sent to the device but only the hash of the transaction, which is the basis for a valid signature. In this case details for the transaction cannot be displayed and verified which is why this is not the preferred mode of operation. In fact, setting hash signing mode is not persistent and needs be set again whenever the user needs it.
