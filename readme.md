# Apate

#### Apate was made by
Love & Code by Oskar Lindgren

## Star This Repository If You Liked It!

---

## Installation 


### 📁・Setting up Apate
1. Start off by installing [python](https://www.python.org/)
2. {pot. change code}
3. Install all modules in `requierments.txt`
4. Eun `setup.bat`

### ⚙・Manually Compiling Source Code
If you prefer to do things on your own run `pip install <every line in requierments.txt>`
*example: `pip install selenium`*
then run this command in a terminal or shell:
```
pyinstaller --onefile --clean --name The_name_you_want main.py
```
3 folders and 1 file will be created, you can delete them all except for the dist folder
go into the dist folder and there is your exe

### 💾・ More options
Add these into the command when creating the exe if you want

|    Pyinstaller Options 		|
| ------------------------------------ 	|
| `-n name` Name that the exe will have (default is the .py file)	|
| `-i icon.ico` Icon that the exe will have (do `-i NONE` for normal executable look)	|
| `--clean` Clean PyInstaller cache and remove temporary files before building	|
| `--uac-admin` Requests admin privileges upon running the exe |
| `--hidden-import MODULENAME` Name an import not visible in the code of the script. Can be used multiple times |
