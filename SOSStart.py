'''
Created on Apr 15, 2019
@author: shivani
'''
import sys
sys.path.insert(0,'/home/raspberry/workspace/iot-device/apps')
print(sys.path)


from labs.module08 import SOSSensor

'''This script initializes the SOS Sensor Adaptor,enables it and starts the process of 
retrieving the accelerometer  data from SenseHat acclereometer Sensors'''
SOSSensor = SOSSensor.SOSSensor()
print("Starting the  Adaptor daemon thread...")


'''This enables the system to access performance readings 
   and starts the multiple threads after regular intervals
'''  
SOSSensor.setEnableEmulatorFlag(True)       
SOSSensor.start() 