'''
Created on Apr 15, 2019
@author: shivani
'''

import sys
sys.path.insert(0,'/home/raspberry/workspace/iot-device/apps')
print(sys.path)

from labs.module08 import SOSActuator

'''This script initializes the accelerometer Sensor actuator, and starts the process of 
subscribing the compass data trigger events from ubidots
'''
SOSActuator = SOSActuator.SOSActuator()
print("Starting the  Adaptor daemon thread...")


'''This enables the system to access triggered events  from ubidots cloud'''        
SOSActuator.start()