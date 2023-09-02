#import your module
import exampleModule

#list will contain all data collection modules
modules = []

#append it to the list of modules
modules.append(exampleModule.exampleModule())

for module in modules:
    module.setup()

running = True
message_length = 64

while(running):

    transmit = ""

    for module in modules:
        transmit += f"[\"{module.module_name}\",  \"{module.poll()}\"]"
    
    for i in range(len(transmit) // message_length + 1):
        message = transmit[i : min( (i + 1) * message_length, len(transmit) )]
        #rmf9x.send_with_ack(bytearray(message))
        print(f"sending: {message}")
