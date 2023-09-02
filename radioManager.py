#import your module
import exampleModule

#list will contain all data collection modules
modules = []

#append it to the list of modules
modules.append(exampleModule())

for module in modules:
    module.setup()

#radio setup
RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.GP5)
RESET = digitalio.DigitalInOut(board.GP6)
spi = busio.SPI(board.GP2, MOSI=board.GP3, MISO=board.GP4)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=3000)

rfm9x.coding_rate = 5
rfm9x.spreading_factor = 8
rfm9x.tx_power = 23
rfm9x.enable_crc = False
rfm9x.node = 200
rfm9x.destination = 201

running = True
message_length = 64 #bytes

while(running):

    transmit = ""

    for module in modules:
        transmit += f"[\"{module.module_name()}\",  \"{module.poll()}\"]"
    
    for i in range(len(transmit) // message_length + 1):
        message = transmit[i : min( (i + 1) * message_length, len(transmit) )]
        rmf9x.send_with_ack(bytearray(message))
        print(f"sending: {message}")
