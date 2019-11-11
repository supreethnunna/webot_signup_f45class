
from credentials import username,pwd,enc_key
from webbot import Browser
from datetime import datetime, date


import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

pwd_encrpyted = encode(enc_key,pwd)

# Open a browser
web = Browser()
# Open the specific link you want to login
link = web.go_to('Enter your f45 mind body url')
#Click on Login
login = web.click('Log in')
# Pass username as input to login
id = web.type(username,into='Email',id='requiredtxtUserName')
# Pass password as input to login
passw = web.type(pwd, into='Password', id='requiredtxtPassword')
#Click on login
login = web.click('Log in')
# Click on appropriate class number you want to signup
signup = web.click('Sign Up Now',number = 5)
# Make the reservation
reserve = web.click('Make a single reservation')
# Logout of the app
logout = web.click('Log Out')
# Quit the browser
web.quit()


#Get todays week number
today = date.today()
weekno = today.weekday()
weekno

# Return class number you want to reserve based on your schedule you would like to come everyday and pass this input to the signup web action
def get_class_num(weekno):
    if (weekno >= 0) and (weekno <= 3):
        return(12)
    elif (weekno == 4):
        return(8)
    elif (weekno == 5):
        return(5)
    else:
        return(8)
