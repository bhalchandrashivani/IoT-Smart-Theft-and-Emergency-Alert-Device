'''
Created on Jan 23, 2019
@author: Shivani
'''

'''This class is used to define the values of constants that can be used in required functions 
   or methods to access meanings of various values such as host , port , address, cloud names
'''
class ConfigConst():
    SECTION_SEPARATOR     = '.'
    
    DEFAULT_CONFIG_FILE_NAME = '/home/pi/workspace/iot-device/config/ConnectedDevicesConfig.props'
    
    DEFAULT_HOST          = '127.0.0.1'
    DEFAULT_COAP_PORT     = 5683
    DEFAULT_MQTT_PORT     = 1883
    SECURE_COAP_PORT      = 5684
    SECURE_MQTT_PORT      = 8883
    DEFAULT_POLL_CYCLES   = 60
    
    CLOUD                 = 'cloud'
    MQTT                  = 'mqtt'
    COAP                  = 'coap'
    SMTP                  = 'smtp'
    GATEWAY_DEVICE        = 'gateway'
    CONSTRAINED_DEVICE    = 'device'
    
    UBIDOTS               = 'ubidots'
    AWS                   = 'aws'
    GCP                   = 'gcp'
    AZURE                 = 'azure'
    
    UBIDOTS_CLOUD_SECTION = UBIDOTS + SECTION_SEPARATOR + CLOUD
    AWS_CLOUD_SECTION     = AWS + SECTION_SEPARATOR + CLOUD
    GCP_CLOUD_SECTION     = GCP + SECTION_SEPARATOR + CLOUD
    AZURE_CLOUD_SECTION   = AZURE + SECTION_SEPARATOR + CLOUD
    SMTP_CLOUD_SECTION    = SMTP + SECTION_SEPARATOR + CLOUD
    MQTT_CLOUD_SECTION    = MQTT + SECTION_SEPARATOR + CLOUD
    COAP_CLOUD_SECTION    = COAP + SECTION_SEPARATOR + CLOUD
    MQTT_GATEWAY_SECTION  = MQTT + SECTION_SEPARATOR + GATEWAY_DEVICE
    COAP_GATEWAY_SECTION  = COAP + SECTION_SEPARATOR + GATEWAY_DEVICE
    MQTT_DEVICE_SECTION   = MQTT + SECTION_SEPARATOR + CONSTRAINED_DEVICE
    COAP_DEVICE_SECTION   = COAP + SECTION_SEPARATOR + CONSTRAINED_DEVICE
    
    CLOUD_API_KEY         = 'apiKey'
    CLOUD_MQTT_BROKER     = 'mqttBroker'
    CLOUD_MQTT_PORT       = 'mqttPort'
    CLOUD_COAP_HOST       = 'coapHost'
    CLOUD_COAP_PORT       = 'coapPort'
    
    FROM_ADDRESS_KEY      = 'fromAddr'
    TO_ADDRESS_KEY        = 'toAddr'
    TO_MEDIA_ADDRESS_KEY  = 'toMediaAddr'
    TO_TXT_ADDRESS_KEY    = 'toTxtAddr'
    
    HOST_KEY              = 'host'
    PORT_KEY              = 'port'
    SECURE_PORT_KEY       = 'securePort'
    
    USER_NAME_TOKEN_KEY   = 'userNameToken'
    USER_AUTH_TOKEN_KEY   = 'authToken'
    
    ENABLE_AUTH_KEY       = 'enableAuth'
    ENABLE_CRYPT_KEY      = 'enableCrypt'
    ENABLE_EMULATOR_KEY   = 'enableEmulator'
    ENABLE_LOGGING_KEY    = 'enableLogging'
    POLL_CYCLES_KEY       = 'pollCycleSecs'
    
    KEEP_ALIVE_KEY        = 'keepAlive'
    '''Added this constant value for nominal temperature'''
    NOMINAL_TEMP          = 'nominalTemp'



    def __init__(self, params):
        '''
        Constructor
        '''
        