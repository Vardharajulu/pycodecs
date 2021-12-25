# pycodecs
Package provides python AVL based Server for Codec 8 and Codec 8 Extended Protocols.
This package will parse the AVL Data and log it in human readable JSON format. Store AVL data as JSON in any data base/store by extending this library.

## prerequisite
Python 3.8+

## How to start codec 8 server
Go to App directory and run python3.8 server.py codec8.

## How to test codec 8 servers with sample client
Go to App directory and run python3.8 client.py codec8.

## How to start codec 8 extended server
Go to App directory and run python3.8 server.py. 
## How to test codec 8 extended server with sample client
Go to App directory and run python3.8 client.py.

## How to add hex file to sample client
Go to data folder and add your customized hex file and update client.py line no 16/19 .

## Codec8 sample input with output

```
000000000000004308020000016B40D57B480100000000000000000000000000000001010101000000000000016B40D5C198010000000000000000000000000000000101010101000000020000252C
```

```
{
    "codec_id": 8,
    "crc_16": "0000252c",
    "records": [
        {
            "events": {
                "event_io_id": 1,
                "n1_of_one_byte_io": 1,
                "n1_of_one_byte_values": [
                    [
                        1,
                        "0"
                    ]
                ],
                "n2_of_two_byte_io": 0,
                "n2_of_two_byte_values": [],
                "n4_of_four_byte_io": 0,
                "n4_of_four_byte_values": [],
                "n8_of_eight_byte_io": 0,
                "n8_of_eight_byte_values": [],
                "total_io_id": 1
            },
            "gps_element": {
                "altitude": 0,
                "angle": 0,
                "gps_element_status": "Invalid GPS Data",
                "latitude": 0,
                "longitude": 0,
                "satellites": 0,
                "speed": 0
            },
            "priority": 1,
            "timestamp": "2019-06-10 10:01:01+00:00"
        },
        {
            "events": {
                "event_io_id": 1,
                "n1_of_one_byte_io": 1,
                "n1_of_one_byte_values": [
                    [
                        1,
                        "1"
                    ]
                ],
                "n2_of_two_byte_io": 0,
                "n2_of_two_byte_values": [],
                "n4_of_four_byte_io": 0,
                "n4_of_four_byte_values": [],
                "n8_of_eight_byte_io": 0,
                "n8_of_eight_byte_values": [],
                "total_io_id": 1
            },
            "gps_element": {
                "altitude": 0,
                "angle": 0,
                "gps_element_status": "Invalid GPS Data",
                "latitude": 0,
                "longitude": 0,
                "satellites": 0,
                "speed": 0
            },
            "priority": 1,
            "timestamp": "2019-06-10 10:01:19+00:00"
        }
    ],
    "records_count": 2,
    "records_count2": 2
}
```

## Codec8 extended sample input with output

```
000000000000004A8E010000016B412CEE000100000000000000000000000000000000010005000100010100010011001D00010010015E2C880002000B000000003544C87A000E000000001DD7E06A00000100002994
```

```
{
    "codec_id": 142,
    "crc_16": "00002994",
    "records": [
        {
            "events": {
                "event_io_id": 1,
                "n1_of_one_byte_io": 1,
                "n1_of_one_byte_values": [
                    [
                        1,
                        "1"
                    ]
                ],
                "n2_of_two_byte_io": 1,
                "n2_of_two_byte_values": [
                    [
                        17,
                        "1d"
                    ]
                ],
                "n4_of_four_byte_io": 1,
                "n4_of_four_byte_values": [
                    [
                        16,
                        "15e2c88"
                    ]
                ],
                "n8_of_eight_byte_io": 2,
                "n8_of_eight_byte_values": [
                    [
                        11,
                        "3544c87a"
                    ],
                    [
                        14,
                        "1dd7e06a"
                    ]
                ],
                "nX_of_x_byte_values": [],
                "nx_of_x_byte_io": 0,
                "total_io_id": 5
            },
            "gps_element": {
                "altitude": 0,
                "angle": 0,
                "gps_element_status": "Invalid GPS Data",
                "latitude": 0,
                "longitude": 0,
                "satellites": 0,
                "speed": 0
            },
            "priority": 1,
            "timestamp": "2019-06-10 11:36:32+00:00"
        }
    ],
    "records_count": 1,
    "records_count2": 1
}
```
