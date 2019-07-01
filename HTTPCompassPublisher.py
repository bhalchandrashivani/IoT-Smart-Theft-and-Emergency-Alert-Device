'''
Created on Apr 15, 2019
@author: shivani
'''
import requests


'''Class to connect securely to your Ubidots device using HTTPS and
     Publish a temperature value to the  variable every minute
'''
class HTTPCompassPublisher(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.TOKEN = 'A1E-nDuSgklKdOve42x5KXvi49lTs3pAi2'
        self.DEVICE_LABEL = "sos"
        self.COMPASS_VAR = "compasssensor"
        self.currentTemp = 0
        self.currentHumidity = 0
        self.DEFAULT_URL = "http://things.ubidots.com/api/v1.6/devices/"
        
    '''Converting sensor reading
        @return: self.payload'''
    def sensorReading(self):
        
        self.currentAngle = self.setReading()       
        self.payload = {self.COMPASS_VAR : self.currentAngle}
        return self.payload
    
    '''Function to enable HTTP post With ApiKey 
        @param data : data to be published
    '''
    def post(self , data):
        self.currentAngle = data       
        self.payload = { self.COMPASS_VAR : self.currentAngle}
        self.url = self.DEFAULT_URL + self.DEVICE_LABEL
        self.headers = {"X-Auth-Token":self.TOKEN, "Content-Type":"application/json"}
        self.req = requests.post(url=self.url, headers=self.headers, json=self.payload )
        self.status = self.req.status_code
        if self.status == 200:
            print("Status Code: " + str(self.status) + "\nPublished SensorData: \n" + str(data))
        else:
            print("[ERROR] Status Code: ", self.status )