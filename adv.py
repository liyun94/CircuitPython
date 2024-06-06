# advertisting data via BThome
import board
import digitalio
import busio
import time
from _bleio import adapter, Attribute, Service, UUID, Characteristic, Descriptor, PacketBuffer
import binascii


DEVICE_NAME = "Send"
print(adapter.address)
class BTHomeAdvertisement:
    _ADV_FLAGS = [0x02, 0x01, 0x06]
    _ADV_SVC_XYDATA = [0x0D, 0x16, 0xD2, 0xFC, 0x40, 0x40, 0x08, 0x0A, 0x03, 0x04, 0x01, 0x02, 0x03, 0x04]

    def _name2adv(self, local_name):
        adv_element = bytearray([len(local_name) + 1, 0x09])
        adv_element.extend(bytes(local_name, "utf-8"))
        return adv_element

    def __init__(self, local_name=None):
        if local_name:
            self.adv_local_name = self._name2adv(local_name)
        else:
            self.adv_local_name = self._name2adv(adapter.name)

    def adv_data(self, x, y):
        adv_data = bytearray(self._ADV_FLAGS)
        adv_svc_data = bytearray(self._ADV_SVC_XYDATA)
        adv_svc_data[-4] = (x) & 0xFF
        adv_svc_data[-3] = (x >> 8) & 0xFF
        adv_svc_data[-2] = (y) & 0xFF
        adv_svc_data[-1] = (y >> 8) & 0xFF
        adv_data.extend(adv_svc_data)
        adv_data.extend(self.adv_local_name)
        print(len(adv_data))
        return adv_data

bthome = BTHomeAdvertisement(DEVICE_NAME)

test_uuid = UUID(0x1234)
test_service = Service(uuid=test_uuid, secondary=False)


while True:
    # the codes below showcases how to send info (x,y) via bthome advertizing
    
    x = 1 & 0xFFFF
    y = 1 & 0xFFFF

    adv_data = bthome.adv_data(x,y)
    adapter.start_advertising(
        data=adv_data, scan_response=None, connectable=True, interval=0.0200001
    )
    time.sleep(1)
        
    adapter.stop_advertising()
    
        

