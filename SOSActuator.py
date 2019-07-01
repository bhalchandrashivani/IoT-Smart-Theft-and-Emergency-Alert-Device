'''
Created on Apr 15, 2019
@author: shivani
'''
from labs.module08 import MqttClientConnectorNew
import time

''' this class is used to subscribe to a particular topic from ubidots cloud
     to receive any alert actuator messages for the changing values of accelerometer
'''
class SOSActuator(object):

    def __init__(self):
        '''
        Constructor initializing to sosalert events variable of SOS device
        '''
        self.ubidots_alert_actuator = "/sosalert"        
        self.ubidots_device = "/sos"
        self.alert_topic = "/v1.6/devices" + self.ubidots_device + self.ubidots_alert_actuator +"/lv"        
        self.client = MqttClientConnectorNew.MqttClientConnectorNew()
    
    
    '''method to connect to client and subscribe to topic'''    
    def start(self):
        try:
            self.client.connect()
            while True:
                self.client.subscibetoTopic(self.alert_topic)
                print("waiting for sosalert")
                time.sleep(6)
        except:
            self.client.disconnect()