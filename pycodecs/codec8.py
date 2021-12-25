import struct
from datetime import datetime, timezone

CEIL_VALUE = 1
PROTOCOL_VERISON = 8

def verify_header(data):
    try:
        preamble = int(data[0:3+CEIL_VALUE].hex(), 16)
        data_field_length = int(data[4:7+CEIL_VALUE].hex(), 16)
        if preamble:
            return False
        else:
            return data_field_length
    except Exception as e:
        print('Invalid Header')
        return False

def process_data(data, length):
    result = {}
    codec_id = int(data[0:1].hex(), 16)                                                    #1 byte
    result['codec_id'] = codec_id
    if codec_id != PROTOCOL_VERISON:
        print('codec_id:{0} Not Supported Data'.format(codec_id))
    else:
        records_count = int(data[1:1+CEIL_VALUE].hex(), 16)                                #1 byte
        result['records_count'] = records_count
        result['records'] = []
        record_start = 2
        result['records'] = []
        for i in range(records_count):
            records = {}   
            timestamp = int(data[record_start:record_start+7+CEIL_VALUE].hex(), 16)
            timestamp = str(datetime.fromtimestamp(timestamp/1000.0, tz=timezone.utc))
            priority  = int(data[record_start+8:record_start+8+CEIL_VALUE].hex(), 16)       #1 bytes
            gps_element	= data[record_start+9:record_start+23+CEIL_VALUE]                   #15 bytes
            longitude = int(gps_element[0:3+CEIL_VALUE].hex(), 16)                          #4 bytes	
            latitude = 	int(gps_element[4:7+CEIL_VALUE].hex(), 16)                          #4 bytes
            altitude = 	int(gps_element[8:9+CEIL_VALUE].hex(), 16)                          #2 bytes
            angle = 	int(gps_element[10:11+CEIL_VALUE].hex(), 16)                        #2 bytes
            satellites =  int(gps_element[12:12+CEIL_VALUE].hex(), 16)                      #1 bytes	
            speed = int(gps_element[13:14+CEIL_VALUE].hex(), 16)                            #2 bytes
            if speed == 0:
                gps_element_status = 'Invalid GPS Data'
            else:
                gps_element_status = 'Valid GPS Data'
            
            for variable in ['timestamp', 'priority']:
                records[variable] = eval(variable)
            records['gps_element'] = {}
            for variable in ['longitude', 'latitude', 'altitude', 'angle', 'satellites', 'speed', 'gps_element_status']:
                records['gps_element'][variable] = eval(variable)
            
            event_io_id = int(data[record_start+24:record_start+24+CEIL_VALUE].hex(), 16)	#1 bytes
            total_io_id = int(data[record_start+25:record_start+25+CEIL_VALUE].hex(), 16)   #1 bytes
            
            n1_of_one_byte_io = int(data[record_start+26:record_start+26+CEIL_VALUE].hex(), 16)	#1 bytes
            n1_of_one_byte_values = []
            slider = record_start+27
            for j in range(n1_of_one_byte_io):
                id  = int(data[slider:slider+CEIL_VALUE].hex(), 16)                        #1 bytes
                value = str(hex(int(data[slider+1:slider+1+CEIL_VALUE].hex(),16)))[2:]       #1 byte
                n1_of_one_byte_values.append((id,value))
                slider = slider+2
                
            n2_of_two_byte_io = int(data[slider:slider+CEIL_VALUE].hex(), 16)	             #1 bytes
            n2_of_two_byte_values = []
            slider = slider+1
            for j in range(n2_of_two_byte_io):
                id  = int(data[slider:slider+CEIL_VALUE].hex(), 16)                        #1 bytes
                value = str(hex(int(data[slider+1:slider+2+CEIL_VALUE].hex(),16)))[2:]       #2 bytes
                n2_of_two_byte_values.append((id,value))
                slider = slider+3

            n4_of_four_byte_io = int(data[slider:slider+CEIL_VALUE].hex(), 16)	         #1 bytes
            n4_of_four_byte_values = []
            slider = slider+1
            for j in range(n4_of_four_byte_io):
                id  = int(data[slider:slider+CEIL_VALUE].hex(), 16)                        #1 bytes
                value = str(hex(int(data[slider+1:slider+4+CEIL_VALUE].hex(),16))) [2:]      #4 bytes
                n4_of_four_byte_values.append((id,value))
                slider = slider+5

            n8_of_eight_byte_io = int(data[slider:slider+CEIL_VALUE].hex(), 16)	         #1 bytes
            n8_of_eight_byte_values = []
            slider = slider+1
            for j in range(n8_of_eight_byte_io):
                id  = int(data[slider:slider+CEIL_VALUE].hex(), 16)                        #1 bytes
                value = str(hex(int(data[slider+1:slider+8+CEIL_VALUE].hex(),16)))[2:]       #8 bytes
                n8_of_eight_byte_values.append((id,value)) 
                slider = slider+9

            events = {}
            for variable in ['event_io_id', 'total_io_id',
                'n1_of_one_byte_io', 'n1_of_one_byte_values',
                'n2_of_two_byte_io', 'n2_of_two_byte_values', 
                'n4_of_four_byte_io', 'n4_of_four_byte_values',
                'n8_of_eight_byte_io', 'n8_of_eight_byte_values']:
                    events[variable] = eval(variable)
            records['events']= events
            result['records'].append(records)            
            record_start = slider
        #d = ''.ljust(length,'B')
        #d = struct.unpack(d, data)
        records_count2 = int(data[record_start:record_start+CEIL_VALUE].hex(), 16)          #1 byte
        result['records_count2'] = records_count2
        crc_16 = str(data[record_start+1:record_start+4+CEIL_VALUE].hex())                  #4 byte
        result['crc_16'] = crc_16
        return result
              
def send_response(conn, length):
    buf = bytes()
    data = struct.pack(">I", length).hex()
    for i in range(0,len(data),2):
        buf += struct.pack('B', int(data[i:i+2],16))
    conn.sendall(buf)

