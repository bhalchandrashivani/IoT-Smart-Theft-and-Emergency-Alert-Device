'''
Created on Apr 15, 2019
@author: shivani
'''
from sense_hat import SenseHat
import threading
import random
from time import sleep
from labs.module08 import MqttClientConnectorNew

'''
    This class enable the accelerometer on sensehat and fetch readings of changing axis
    and publishing data to ubidots cloud using mqtt
'''
class SOSSensor(object):

    def __init__(self):
        '''
        Constructor : Initializing Compass Sensor and Sensehat
        and setting ubidots variables and topic's values 
        '''
        self.sensehat = SenseHat()
        self.waitInSec = 1
        self.red =(255,0,0)
        self.CompassSensorData = "Compass Sensor"
        self.ubidots_accel_Var = "/accelsensor"     #ubidots device variable for accelometer 
        self.ubidots_alert_actuator = '/sosalert'   #ubidots actuator variable SOS alert
        self.ubidots_device = "/sos"                #ubidots device name
        self.ubidots_accel_topic = "/v1.6/devices" + self.ubidots_device + self.ubidots_accel_Var
        self.alert_topic = "/v1.6/devices" + self.ubidots_device + self.ubidots_alert_actuator
        self.mqttClient = MqttClientConnectorNew.MqttClientConnectorNew()
        self.motion = 0
        self.setangle = 0
     
        
    '''Enabling the emulator
      @param enableEmulator:  Defaults to false; if true will enable emulator to run
    '''
    def setEnableEmulatorFlag(self , enableEmulator ):
        self.enableEmulator = enableEmulator
    
    
    '''Running accelerometer sensor and connecting with the mqtt client
    '''   
    def run(self):
            self.mqttClient.connect();
            while True:
                if self.enableEmulator:
                    '''accepting  accelerometer raw value from SenseHat by setting IMU config,
                       converting it to a fix value to avoid the lag 
                       and sending it to MQTTClientConnector to send over ubidots cloud
                    ''' 
                    self.sensehat.set_imu_config(False, False, True)  
                    while True:
                        self.motion = self.sensehat.get_accelerometer_raw()                       
                        x = self.motion['x']
                        y = self.motion['y']
                        z = self.motion['z']
                        x=round(x,0)
                        y=round(y,0)
                        z=round(z,0)
                        print("x={0},z={1}".format(x, z))
                        
                        '''generating values from given range for demo reasons for alert and normal axes''' 
                        if z==-1.0 :
                            self.setangle = random.uniform(1,5)
                            print("alert axis %s" % self.setangle)
                        else:
                            self.setangle = random.uniform(6,10)
                            print(" normal axis %s" % self.setangle)                        
                        self.mqttClient.publishMessage(self.ubidots_accel_topic, self.setangle, 2)
                        sleep(0.5)
    
    
    '''defining thread and its parameter.
    the thread will execute run function which does the job
    ''' 
    def start (self):   #
        t = threading.Thread( target= self.run())
        t.start()