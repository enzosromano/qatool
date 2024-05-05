# QATool - Enzo Romano

## Dont know where to start with automation? Why not start here!

QATool is a simple low maintenance solution to begin automating basic tasks.  
Whether you are a developer, QA, Project Manager... This serves as a simple template to build upon to easily run automation scripts with Python + Selenium.  

While you still have to write the scripts yourself, this project allows you to already have a simple file structure setup alongside an easily 
customizable GUI (with tkinter) to call your scripts from within an application.  

## Prerequisites
### Python 3 - https://www.python.org/downloads/

## After cloning the repo:
### First, 
ensure you have access to `pip`, which you should have received alongside Python.  
You can verify this by opening a command prompt and runing `pip --version`.  

### If you have pip, you must now install selenium and pytest
Selenium: `pip install selenium`  
Pytest: `pip install pytest`
Pyinstaller: `pip install -U pyinstaller`
  
### Lastly,  
assuming you will be using Chrome, you must download the chrome driver for your browsers current version.  
Check your current browser version by opening Chrome, clicking on the settings menu in the top right, and opening the about menu.  
![about img](https://www.lifewire.com/thmb/bKfZs55XrYQ0lmMRRcqUnc6VWsE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/A2-CheckWhatVersionofChromeYouHave-annotated-f43c6e8eb4c142f28340b5d9a900a795.jpg)  
  
Chrome version 115 or newer: https://googlechromelabs.github.io/chrome-for-testing/  
Chrome version 114 and under: https://chromedriver.chromium.org/downloads  

(If you are opting to use another browser, please consult the relevant browsers documentation.)  
  
Once you have the driver downloaded, drag it from the download location into your projects root folder  
(Same level as src, but not within src)  

## Run It!  
This project will be run from the main.py file. You can either execute main.py manually from the terminal, or by simply opening up the file in a Python supported ide and running it.
  
To do it from the terminal, open up a terminal within the root and run `cd src/`, followed by `python main.py`.  
The application should open.  

## I want to make this into a .exe:  

Thanks to pythons built in libraries, pyinstaller has you covered!  

To create a .exe, run `pyinstaller file_name.py`. (Ensure you ran `npm install` during setup, or it may ask you to install the dependency on your machine first.)  
If you havent changed the name of main.py, file_name.py would be referencing main.py, where the app itself exists.  
