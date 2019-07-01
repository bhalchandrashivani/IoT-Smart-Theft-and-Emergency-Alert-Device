'''
Created on Jan 20, 2019
@author: Shivani Bhalchandra
'''
import smtplib
'''from labbenchstudios.common import ConfigConst'''
from labs.module08 import ConfigUtil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''This function is a SMTP connector used to send email or SMS alerts once they are triggered by the emulator'''

class SmtpClientConnector():
    ConfigConst = None

    def __init__(self):
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfig()
        print("test")
    
    '''Fetchin and setting all the required values from Congif Constant necessary 
      to make a SMTP connection and send email or sms '''
        
    def test(self , key):
        return  self.key   
    def publishMessage(self, topic, data):
        print("problem")   
        try:  
            host = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.HOST_KEY)
            port = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.PORT_KEY)
            fromAddr = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.FROM_ADDRESS_KEY)
            toAddr = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.TO_ADDRESS_KEY)
            authToken = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.USER_AUTH_TOKEN_KEY)
            
            '''sending sms alert details setting'''
            msg = MIMEMultipart()
            msg['From'] = fromAddr
            msg['To'] = toAddr
            msg['Subject'] = topic
            msgBody = str(data)
            msg.attach(MIMEText(msgBody))
            msgText = msg.as_string()
            
            
            '''sending email alert details setting, sending hello to server ,
             logging in email id , sending email and logging out'''
            smtpServer = smtplib.SMTP_SSL(host, port)
            smtpServer.ehlo()
            smtpServer.login(fromAddr, authToken)
            smtpServer.sendmail(fromAddr, toAddr, msgText)
            smtpServer.close()
        except:
            print("problem")