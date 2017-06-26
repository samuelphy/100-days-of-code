import pygatt
import logging

# Comment logging to disable debug log in console
logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.DEBUG)


DEVICE_ADDRESS = "00:0E:0B:14:35:11"
# Many devices, e.g. Fitbit, use random addressing - this is required to
# connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect(DEVICE_ADDRESS, address_type=ADDRESS_TYPE)
    value = device.char_write_handle(13, bytearray([0xFF, 0xE0, 0x6F])) #65 = ON, 6F = OFF
    #value = device.char_read("00001800-0000-1000-8000-00805f9b34fb")
finally:
    adapter.stop()
