# using adapter fucntion scan for bluetooth devices 
# writed by LI YUN
import board
import digitalio
from _bleio import adapter, Attribute, Service, UUID, Characteristic, Descriptor, PacketBuffer
import binascii

while True:
    
    for advertisement in adapter.start_scan(interval=0.01,window = 0.005):
        data = advertisement.advertisement_bytes
        if b'Send' in data:
            print(binascii.hexlify(data))
            adapter.stop_scan()
        else:    
            adapter.stop_scan()


    
    
    
