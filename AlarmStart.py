'''
Created on Apr 15, 2019
@author: shivani
'''
import sys
sys.path.insert(0,'/home/raspberry/workspace/iot-device/apps')
#sys.path.insert(1,'/usr/lib/python2.7/dist-packages/')
print(sys.path)


from labs.module08 import AlarmSensor

'''This script initializes the Alarm Sensor Adaptor,enables it and starts the process of 
retrieving the Magnetometer  data from SenseHat magnetometer Sensors
'''
AlarmSensor = AlarmSensor.AlarmSensor()
print("Starting the  Adaptor daemon thread...")


'''This enables the system to access performance readings 
   and starts the multiple threads after regular intervals
'''  
AlarmSensor.setEnableEmulatorFlag(True)       
AlarmSensor.start()