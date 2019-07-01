'''
Created on Apr 15, 2019
@author: shivani
'''
import sys
sys.path.insert(0,'/home/raspberry/workspace/iot-device/apps')
#sys.path.insert(1,'/usr/lib/python2.7/dist-packages/')
print(sys.path)

from labs.module08 import AlarmActuator

'''This script initializes the compass Sensor actuator, and starts the process of 
subscribing the compass data trigger events from ubidots
'''
AlarmActuator = AlarmActuator.AlarmActuator()
print("Starting the  Adaptor daemon thread...")


'''This enables the system to access triggered events  from ubidots cloud'''         
AlarmActuator.start()