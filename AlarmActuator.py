'''
Created on Apr 15, 2019
@author: shivani
'''
from labs.module08 import MqttClientConnectorNew
import time


''' this class is used to subscribe to a particular topic from ubidots cloud
     to receive any alert actuator messages for the changing values of compass
'''
class AlarmActuator(object):

    def __init__(self):
        '''
        Constructor initializing to alert events variable of SOS device
        '''
        self.ubidots_alert_actuator = "/alert"       
        self.ubidots_device = "/sos"
        self.alert_topic = "/v1.6/devices" + self.ubidots_device + self.ubidots_alert_actuator +"/lv"
        self.client = MqttClientConnectorNew.MqttClientConnectorNew()
    
    
    '''method to connect to client and subscribe to topic'''      
    def start(self):
        try:
            self.client.connect()
            while True:
                self.client.subscibetoTopic(self.alert_topic)
                print("waiting for alarm")
                time.sleep(6)
        except:
            self.client.disconnect()