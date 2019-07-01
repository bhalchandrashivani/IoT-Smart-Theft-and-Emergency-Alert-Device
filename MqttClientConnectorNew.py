'''
Created on Apr 16, 2019
@author: shivani
'''  
  
import time
import paho.mqtt.client as mqttClient
from labs.module08 import ConfigUtil
from labs.module08 import SensorData

from labs.module02 import SmtpClientConnector
from labs.module03 import SenseHatLedActivator
import ssl
from datetime import datetime
from labs.module08 import SOSLed

class MqttClientConnectorNew(object):
    
    '''
    mqtt connector
    Functions to connect to broker, subscribe message , publish message
    disconnect from broker 
    @param port: the port to which broker is conencted
    @param brokerAddr: the domain name of broker
    @param mqttClient: instance variable for MqttClient
    @param config: instance variable for ConfigUtil class   
    '''
    port = None
    brokerAddr=""
    brockerKeepAlive = None
    mqttClient=None
    config = None
    

    def __init__(self):
        '''
        Constructor
        '''
        self.mqttClient = mqttClient.Client()
        self.config = ConfigUtil.ConfigUtil()
        self.sensoData = SensorData.SensorData()
        self.config.loadConfig()
        self.brockerKeepAlive = 60
        self.connected_flag = False
        
        self.pemfile = "/home/raspberry/workspace/ubidots_cert.pem"
        self.authToken = 'A1E-nDuSgklKdOve42x5KXvi49lTs3pAi2'
        self.port = 8883
        self.brokerAddr = 'things.ubidots.com'
        self.password = ''
        
        self.smtp = SmtpClientConnector.SmtpClientConnector()
        self.timeStamp = str(datetime.now())
        self.senseled = SOSLed.SOSLed()
        self.sensehatled = SenseHatLedActivator.SenseHatLedActivator()
        
                 
    '''
        Function to connect to mqtt broker
    '''
    def connect(self, connectionCallback = None , msgCallback = None):

        #Setting the right callbacks
        if(connectionCallback!=None):
            self.mqttClient.on_connect = connectionCallback
        else:
            self.mqttClient.on_connect = self.onConnect
            
        if(msgCallback !=None) :
            self.mqclient.on_disconnect = msgCallback
        else :
            self.mqttClient.on_disconnect = self.onMessage
        #callback when message arrives
        self.mqttClient.on_message = self.onMessage    
        print("Connecting to broker",self.brokerAddr)
        #connect to broker
        self.mqttClient.username_pw_set(self.authToken, self.password)
        self.mqttClient.tls_set(ca_certs = self.pemfile, certfile = None, keyfile = None, cert_reqs = ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        self.mqttClient.tls_insecure_set(False)
        self.mqttClient.connect(self.brokerAddr, self.port, self.brockerKeepAlive)
        self.mqttClient.loop_start() 
        while not self.connected_flag:
            print("Attempting to connect to broker :",self.brokerAddr)
            time.sleep(1)
    
    
    '''
        function to disconnect from broker
    '''    
    def disconnect(self):
        print("Disconneting the MQTT  broker connection ")
        self.mqttClient.disconnect()

    
    '''
        callback when the connection is made with broker
        @param rc: return code for connection  
    '''    
    def onConnect(self , client ,userData , flags , rc):        
        if rc == 0:
            self.connected_flag = True
            print("Connected OK returned Code:" , rc)
        else:
            print("Bad connection Returned Code:", rc)
            
    
    '''
        callback when message arrives 
        payload 1: publish Burglar alert email
        payload 10 : publish SOS alert email
    '''        
    def onMessage(self , client ,userdata , msg):

        if msg.payload=='1' :
            print("ALERT ::Topic is " +msg.topic + "-->" + str(msg.payload))
            self.smtp.publishMessage("Attempt to open Safe : Burglar Alert", "Please call security")
            self.senseled.show_burglarmsg()
        
        elif msg.payload=='10':
            print("ALERT ::Topic is " +msg.topic + "-->" + str(msg.payload))
            self.smtp.publishMessage("SOS Alert", "Contact Immediately")
            self.senseled.show_sosmsg()
            
        else:
            print("still")
            self.senseled.clearmessage()
                    
        
    '''        
        function to publish message
        @param topic: name of the topic to publish message
        @param msg: The message to be sent   
    '''    
    def publishMessage(self , topic , msg , qos=2):

        print("Publishing: ",msg)
        print("topic" , topic)
        self.mqttClient.publish(topic, msg, qos)
        

    '''
        function to subscribe to a topic
        @param topic: name of the topic to subscribe to 
        @param connectionCallback:   
    '''
    def subscibetoTopic(self , topic ,connnectionCallback = None, qos=2):
 
        if connnectionCallback != None:
            self.mqttClient.on_subscribe = (connnectionCallback)
            self.mqttClient.on_message = (connnectionCallback)
        self.mqttClient.subscribe(topic , qos)
        
    
    '''
        function to unsubscribe to a topic
    '''    
    def unsubscibefromTopic(self , topic):
        
        print("Unsubscribing from topic",topic)
        self.mqttClient.unsubscribe(topic)