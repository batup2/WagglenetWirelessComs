#"module" is not the final name for this interface
#every data generating device (camera, microphone, thermometer) 
#should have its own module class which implements setup and
#poll functions

import random
import time

#dummy class representing a generic sensor, not required
class exampleSensor():
    def read_data(self):
        data = [random.randint(0, 9999) for i in range(0, 10)]
        return data

class exampleModule():
    module_name = "example" #put the name of your sensor/project here
    sensor = None
    polling_interval = 0.5 #time between polls in seconds
    last_poll = time.thread_time()

    def __init__(self):
        print(f"instance of {self.module_name} created")

    def setup(self):
        self.sensor = exampleSensor()

    def wrap_poll(self):
        if (time.thread_time() - self.last_poll) >= self.polling_interval:
            self.last_poll = time.thread_time()
            return self.poll()
        return None


    def poll(self):
        sensor_data = self.sensor.read_data()

        #test of exception handling
        if(random.randint(0, 50) == 42):
            raise Exception("the magic number has been found")
        
        return sensor_data