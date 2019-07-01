'''
Created on Apr 15, 2019
@author: shivani
'''
from sense_hat import SenseHat

'''this class activates sensehat to show messages on led'''
class SOSLed(object):
    def __init__(self):
        self.sensehat = SenseHat()
        self.green =(0,255,0)

    '''display burglar alert message'''
    def show_burglarmsg(self):
        self.sensehat.show_message("! Burglar Alert",text_colour=[255, 0, 0])
    
    '''clear message display "G" for good and no issues'''
    def clearmessage(self):
        self.sensehat.clear()
        self.sensehat.show_letter("G",self.green)
    
    '''display sos alert message'''
    def show_sosmsg(self):
        self.sensehat.show_message("*SOS*",text_colour=[255, 0, 0])
        