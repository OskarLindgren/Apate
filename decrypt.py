import os
from cryptography.fernet import Fernet
from tkinter import *

os.chdir("C:/test_oskar/ligma/balls")
dir = os.getcwd()
key_location = "C:\Key_location"

files = []

the_key = f"{key_location}\key.key"

print("file:", __file__)

for file in os.listdir():
    if file == "stuff.py":
        continue
    if file == "key.key":
        continue
    if os.path.isfile(file):
        files.append(file)
    
with open(the_key, "rb") as key:
    secretkey = key.read()
    
password = "Tablecloth"

user_password = input("Enter the password to get your files back:\n")

if user_password.lower() == user_password.lower(): # if user_password.lower() == password.lower():
    for file in files:
        with open(file, "rb") as cur_file:
            contents = cur_file.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as cur_file:
            cur_file.write(contents_decrypted)
    print("Your files are back! The password was:", password, "You wrote:", user_password)
    os.remove(f"{key_location}\key.key")
    
else:
    print("That's the wrong password")
    
    
input()
