import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    print("You are an admin, continueing program...")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


import os
import shutil

file_dir = os.path.dirname(os.path.abspath(__file__))

# return a list of all directories in C:
def dir_checker(dir=str):   
    
    try:
        os.chdir(dir)
    except Exception:
        print(f"The directory '{dir}' doesn't exist.")
        return
    files = []
    
    for cur in os.listdir(dir):
        files.append(cur)
        
    print(f"files = {files}")
    
dir_checker(input("dir\n"))

locations = ['C:/Users/Emma Lindberg/OneDrive/Desktop']

for location in locations:
    location = location.replace("/", "\\")
    try:
        shutil.copy(f"{__file__}", location)
        print(f"Copied {__file__} to {location}")
    except Exception as e:
        print(e)
        continue
    
