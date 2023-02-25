from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.exceptions import ApiException
import sys 
import os
import time
import requests
import phonenumbers
import pyfiglet
import datetime
import json
#### colours ####
# B='\033[1;94m'
# R='\033[1;91m'
# G='\033[1;92m'
# W='\033[1;97m'
# S='\033[1;96m'
# P='\033[1;95m'
# Y='\033[1;93m'
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'


Omotosho ="""\033[1;91m




  /$$$$$$                /$$           /$$       /$$                              /$$$$$$    /$$     /$$                         /$$      
 /$$__  $$              |__/          | $$      |__/                             /$$__  $$  | $$    | $$                        | $$      
| $$  \__/ /$$$$$$/$$$$  /$$  /$$$$$$$| $$$$$$$  /$$ /$$$$$$$   /$$$$$$         | $$  \ $$ /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$$| $$   /$$
|  $$$$$$ | $$_  $$_  $$| $$ /$$_____/| $$__  $$| $$| $$__  $$ /$$__  $$ /$$$$$$| $$$$$$$$|_  $$_/|_  $$_/   |____  $$ /$$_____/| $$  /$$/
 \____  $$| $$ \ $$ \ $$| $$|  $$$$$$ | $$  \ $$| $$| $$  \ $$| $$  \ $$|______/| $$__  $$  | $$    | $$      /$$$$$$$| $$      | $$$$$$/ 
 /$$  \ $$| $$ | $$ | $$| $$ \____  $$| $$  | $$| $$| $$  | $$| $$  | $$        | $$  | $$  | $$ /$$| $$ /$$ /$$__  $$| $$      | $$_  $$ 
|  $$$$$$/| $$ | $$ | $$| $$ /$$$$$$$/| $$  | $$| $$| $$  | $$|  $$$$$$$        | $$  | $$  |  $$$$/|  $$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$
 \______/ |__/ |__/ |__/|__/|_______/ |__/  |__/|__/|__/  |__/ \____  $$        |__/  |__/   \___/   \___/   \_______/ \_______/|__/  \__/
                                                               /$$  \ $$                                                                  
                                                              |  $$$$$$/                                                                  
                                                               \______/                                                                   




                                                           \033[1;92mCoded by Omotosho Gbolahan Hammed  
                                                           \033[1;93mGithub: https://github.com/Gbolahanomotosho                                                          
                                                           \033[1;94mFacebook: Facebok.com/Gbolahanomotosho
                                                           \033[1;95mInstagram: _lord_of_hacker        
                                                           \033[1;96mWhatsapp: 08022648626
                                                            
                                                           
                                                           
                                                              
                                                           \033[1;96mThis is a simple script which allow you to perform a smishing attack
                                                           \033[1;95ma type of social engineering tricks by impersonating different number 
                                                           \033[1;94mas the sender
                                                              
                                                               
                                                           
                                                           \033[1;93mNB: For ethical purpose only
                                      


\033[1;91m"""






for i in Omotosho:
        time.sleep(0.01)
        print(i, end='',flush=True)




os.system('clear')


attacker = input("\033[1;92mEnter sender/impersonator name: ")

phone_number= input("\033[1;93mEnter your victim phone number with country code e.g +234 09045678934: ")

if  phone_number == "+234 08022648626" or "+23408022648626":
            exit("\033[1;96mSmishing attack cant work on me  😂😂😂😂😂😂😂😂😂  \033[1;91mI am the developer, so respect yourself")
elif phone_number != "+234 08022648626" or "+23408022648626": pass 


text_message = input("\033[1;95mEnter your crafted text message: ")

def Configuration():

    BASE_URL = "https://mpvr96.api.infobip.com"
API_KEY = "2d86b648c363a5e6562e74e84a832fb4-ab0a6e77-7860-4b6f-95ea-aee61aab437f"
        
client_config = Configuration(
            host= BASE_URL,
            api_key={"APIKeyHeader": API_KEY},
            api_key_prefix={"APIKeyHeader": "App"},
    )

api_client = ApiClient(client_config)

sms_request = SmsAdvancedTextualRequest(
                messages=[
                    SmsTextualMessage(
                        destinations=[
                            SmsDestination(
                                to=phone_number,
                            ),
                        ],
                        _from=attacker,
                        text=text_message,
                    )
                ])

api_instance = SendSmsApi(api_client)

try:
            api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
            print(api_response)
except ApiException as ex:
            print("Bad request, Error occurred while trying to send SMS message.")
            print(ex)
            


































