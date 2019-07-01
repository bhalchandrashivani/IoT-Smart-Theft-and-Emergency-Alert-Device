'''
Created on Apr 15, 2019
@author: shivani
'''
from sense_hat import SenseHat
import threading
from time import sleep
from labs.module08 import MqttClientConnectorNew
from labs.module08 import HTTPCompassPublisher

'''
    This class enable the compass on sensehat and fetch readings of changing magnetic field
    and publishing data to ubidots cloud using http
'''
class AlarmSensor(object):


    def __init__(self):
        '''
        Constructor : Initializing Compass Sensor and Sensehat
        and setting ubidots variables and topic's values
        
        '''
        self.sensehat = SenseHat()
        self.waitInSec = 1
        self.red =(255,0,0)
        self.CompassSensorData = "Compass Sensor"
        self.ubidots_Compass_Var = "/compasssensor"  #ubidots device variable
        self.ubidots_alert_actuator = '/alert'       #ubidots actuator variable
        self.ubidots_device = "/sos"                 #ubidots device name
        self.ubidots_compass_topic = "/v1.6/devices" + self.ubidots_device + self.ubidots_Compass_Var
        self.alert_topic = "/v1.6/devices" + self.ubidots_device + self.ubidots_alert_actuator
        self.mqttClient = MqttClientConnectorNew.MqttClientConnectorNew()
        self.motion = 0
        self.setangle = 0
        self.http = HTTPCompassPublisher.HTTPCompassPublisher()
    
        
    '''Enabling the emulator
      @param enableEmulator:  Defaults to false; if true will enable emulator to run
    '''
    def setEnableEmulatorFlag(self , enableEmulator ):
        self.enableEmulator = enableEmulator
    
    
    '''Running compass sensor
    '''   
    def run(self):
            while True:
                if self.enableEmulator:
                    
                    '''accepting  compass value from SenseHat by setting IMU config,
                       converting it to a fix value to avoid the lag 
                       and sending it to httpCompasspublisher to send over cloud
                    '''                    
                    self.sensehat.set_imu_config(True, False, False)
                    while True:
                        self.motion = self.sensehat.get_compass() 
                        print("actual  %s" % self.motion)
                        
                        '''normal angle =200 and alert angle=150'''
                        if self.motion>250 or self.motion<80 :
                            self.setangle = 150
                            print("alert angle %s" % self.setangle)
                        else:
                            self.setangle = 200
                            print(" normal angle %s" % self.setangle)                        
                        self.http.post(self.setangle) # posting data to cloud                        
                        sleep(0.5)
                        
    
    '''defining thread and its parameter.
    the thread will execute run function
    ''' 
    def start (self):   #
        t = threading.Thread( target= self.run())
        t.start()