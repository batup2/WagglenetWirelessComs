#"module" is not the final name for this interface
#every hive sensor should have its own module class which implements setup and
#poll functions

import random

class exampleModule():
    module_name = "example module" #put the name of your sensor/project here
    example_sensor = None
    def __init__(self):
        print("instance of {module name} created")

    def setup():
        example_sensor = exampleSensor()

    def poll():
        sensor_data = exampleSensor.read_data()
        return str(sensor_data)


#dummy class for demonstration purposes
class exampleSensor():
    def read_data():
        return random.randint()