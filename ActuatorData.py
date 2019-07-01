'''
Created on Jan 30, 2019
@author: shivani
'''

import os
from datetime import datetime
from labs.module03 import SenseHatLedActivator

'''defining constant command values'''
COMMAND_OFF = 0
COMMAND_ON = 1
COMMAND_SET = 2
COMMAND_RESET = 3
STATUS_IDLE = 0
STATUS_ACTIVE = 1
ERROR_OK = 0
ERROR_COMMAND_FAILED = 1
ERROR_NON_RESPONSIBLE = -1

'''This class receives the details of temperature variations from the temperature Adaptor
    and processes the request to trigger alerts on the sensHat LED activator
'''
class ActuatorData():
    timeStamp = None
    name = 'Not set'
    hasError = False
    command = 0
    errCode = 0
    statusCode = 0
    stateData = None
    val = 0.0
    
    '''Constructor initializing all required values SensHAtActivator and timestamp
    '''
    def __init__(self):
        self.updateTimeStamp()
        self.sensehat = SenseHatLedActivator.SenseHatLedActivator()
    
    
    '''functions to return command of actuator triggering
    @return: command'''   
    def getCommand(self):
        return self.command

    '''functions to return name of actuator triggering
    @return: name'''
    def getName(self):
        return self.name


    '''functions to return stateData of actuator triggering
    @return: stateData'''
    def getStateData(self):
        return self.stateData


    '''functions to return statusCode of actuator triggering
    @return: statusCode'''
    def getStatusCode(self):
        return self.statusCode


    '''functions to return errCode of actuator triggering
    @return: errCode'''
    def getErrorCode(self):
        return self.errCode
    
    
    '''functions to return val of actuator triggering
    @return: val'''
    def getValue(self):
        return self.val;
    
    
    '''functions to return hasError of actuator triggering
    @return: hasError'''
    def hasError(self):
        return self.hasError
    
    
    '''functions to set different values of actuator processing 
    @param: command'''      
    def setCommand(self, command):
        self.command = command
    
    
    '''functions to set name of actuator processing 
    @param: name '''
    def setName(self, name):
        self.name = name
    
    
    '''functions to set stateData values of actuator processing 
    @param: stateData '''
    def setStateData(self, stateData):
        self.stateData = stateData
    
    
    '''functions to set different values of actuator processing 
    @param: statusCode'''
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
    
    
    '''functions to set errCode of actuator processing 
    @param: errCode  is not 0 hasError=True; hasError=False'''
    def setErrorCode(self, errCode):
        self.errCode = errCode    
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
    
    
    '''functions to set val of actuator processing 
    @param: val'''
    def setValue(self, val):
        self.val = val
    
    
    '''Will store the changed value to the instance of ActuatorData
        @param data: instance of ActuatorData
        setting all values that have been set by getting them from passes parameter
    '''
    def updateData(self, data):
        self.command = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode = data.getErrorCode()
        self.stateData = data.getStateData()
        self.val = data.getValue()
    
    
    '''updating timestamp'''   
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
    
    
    '''Processes the data sent from tempAdaptor ,analyzing if it increased or decreased 
       Triggering SenseHatLed accordingly to display the required message through GPIO
    '''  
    def processMessage(self , data):
        '''If the value is more than nominal temperature : Decrease it'''
        if(data.getValue()>0):
            self.updateData(data)
            self.setCommand("Decrease")
            self.updateTimeStamp()
            print(self.__str__())
            print("\n" + str(self.getCommand()) + " the temperature by " + str(int(data.getValue()))+ " degrees")
            '''Triggering the SenseHatLedActivator'''
            self.sensehat.setEnableLedFlag(True)
            self.sensehat.setDisplayMessage(self.__str__(self))
            self.sensehat.run(self.sensehat)
            
        else:
            '''If the value is less than nominal temperature : Increase it'''
            if(data.getValue()<0):
                self.updateData(data)
                self.setCommand("Increase")
                self.updateTimeStamp()
                print(self.__str__())
                print("\n" + str(self.getCommand()) + " the temperature by " + str(abs(data.getValue())) + " degrees")
                '''Triggering the SenseHatLedActivator'''
                self.sensehat.setEnableLedFlag(True)
                self.sensehat.setDisplayMessage(self.__str__(self))
                self.sensehat.run(self.sensehat)
               
            else:
                '''Keep flashing 'R' trigger'''
                self.sensehat.setEnableLedFlag(True)
                self.sensehat.setDisplayMessage(None)
                self.sensehat.run(self.sensehat)   
            
        
    '''Format to display message'''
    def __str__(self):

        customStr = \
            str('\n-------Actuator reading------ \n' + self.name + ':' + \
            os.linesep + '\tTime: ' + self.timeStamp + \
            os.linesep + '\tCommand: ' + str(self.command) + \
            os.linesep + '\tStatus Code: ' + str(self.statusCode) + \
            os.linesep + '\tError Code: ' + str(self.errCode) + \
            os.linesep + '\tState Data: ' + str(self.stateData) + \
            os.linesep + '\tValue: ' + str(abs(self.val)))
        return customStr
    