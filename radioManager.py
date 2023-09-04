import sys
import time
#import your module
import exampleModule

#list will contain all data collection modules
modules = []

#append it to the list of modules
modules.append(exampleModule.exampleModule())

for module in modules:
    #always use try except when calling module functions to prevent one module
    # from crashing the whole program
    try:
        module.setup()
    except:
        print(f"an exception occurred while setting up {module.name}")

running = True
message_length = 64

while(running):
    transmit = ""
    for module in modules:
        try:
            poll_result = module.wrap_poll()
            if (poll_result is not None):
                transmit += f"[\"{module.module_name}\",  \"{poll_result}\"]"
        except:
            e = sys.exception()
            transmit += f"an exception occurred when polling module \"{module.module_name}\" \n{e}"

    
    for i in range(len(transmit) // message_length + 1):
        message = transmit[i : min( (i + 1) * message_length, len(transmit) )]

        if message != "":
            #rmf9x.send_with_ack(bytearray(message))
            print(f"sending: {message}")
