/*******************************************************************************
*   Ledger MARO App
*   (c) 2016-2019 Ledger
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License.
********************************************************************************/

#ifndef _CHAIN_CONFIG_H_
#define _CHAIN_CONFIG_H_

#include <stdint.h>

#include "os.h"

typedef enum chain_kind_e {
	CHAIN_KIND_MARO
} chain_kind_t;

typedef struct chain_config_s {
	const char* coinName; // ticker
	uint32_t chainId;
	chain_kind_t kind;
#ifdef TARGET_BLUE
    const char* header_text;
    unsigned int color_header;
    unsigned int color_dashboard;
#endif // TARGET_BLUE

} chain_config_t;

#endif /* _CHAIN_CONFIG_H_ */
