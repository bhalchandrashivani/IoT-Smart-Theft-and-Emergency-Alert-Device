'''
Created on Apr 15, 2019
@author: shivani
'''
import os
from datetime import datetime

'''This class stores the aggregated sensor data 
   and also tracks updates of all temperature'''
class SensorData():
    
    timeStamp = None
    name = 'Not set'
    curValue = 20
    avgValue = 10
    minValue = 10
    maxValue = 30
    totValue = 40
    sampleCount = 1
    
    '''Constructor . Setting the timestamp
    '''
    def __init__(self):
        self.timeStamp = str(datetime.now())
        
    
    '''This function counts the no of samples, sets the timestamp,current temperature value and total value.
     Also calculates the average
     @param newVal: setting current value to new val and adding it to the totalvalue 
     '''   
    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = newVal
        self.totValue += newVal
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
        if (self.totValue != 0 and self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount
            
    
    '''functions to return average values of temperature
     @return: avgValue'''   
    def getAvgValue(self):
        return self.avgValue
    
    
    '''functions to return maxValue values of temperature
     @return: maxValue'''
    def getMaxValue(self):
        return self.maxValue
    
    
    '''functions to return minValue values of temperature
     @return: minValue'''
    def getMinValue(self):
        return self.minValue
    
    
    '''functions to return curValue values of temperature
     @return: curValue'''
    def getValue(self):
        return self.curValue
    
    
    '''functions to set name of customer
     @param: name'''
    def setName(self, name):
        self.name = name
    
        
    '''functions to return name of customer
        @return: name'''   
    def getName(self):
        return self.name
        
        
    '''function to print the details of temperature readings and calculated values
    @return: Customer Data formated in readable way
    '''
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime: ' + self.timeStamp + \
            os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + \
            os.linesep + '\tSamples: ' + str(self.sampleCount) + \
            os.linesep + '\tMin: ' + str(self.minValue) + \
            os.linesep + '\tMax: ' + str(self.maxValue))
        return customStr