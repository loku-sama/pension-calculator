# Basic Retirement Benefit Calculator
![GitHub release (latest by date)](https://img.shields.io/github/v/release/loku-sama/pension-calculator) ![GitHub](https://img.shields.io/github/license/loku-sama/pension-calculator)  <a href="https://sourceforge.net/projects/pension-calculator/files/latest/download"><img alt="Download Pension-Calculator" src="https://img.shields.io/sourceforge/dt/pension-calculator.svg" ></a><br/>
A simple retirement benefit calculator app written in python with GUI specifically for West Bengal State Govt. employees (India).
This app is not associated with Govt. of West Bengal. This app is for informational purpose only. 
This project is open source under GNU public lisence v3.0

# Whats New :
## Whats new in Version 1.2.0 : 
# New Features :
1. Dynamic Report Generation : Previously you can only generate one report of each category and the next generated report will autometically replace the previous report. In the latest version this limitation is over. Now you can generate as many reports you want. All the reports will be saved in the reports folder in the main app directory.

2. Update Checker : In the latest release, an autometic update checker is added to the app. It will check for any new releases from GitHub api and notify you. Also you can check manually for any updates from the Help menu. (You will need an active Internet connection for that.)

3. Feedback Option : Now you can directly submit any feedback about the application from Contact menu.

## Version 1.1.0 : 
Now commuted value of pension calculation is added in the pension calculation section. Just input your age as on next birthday to get CVP amount as per applicable factors. Please refer G.O. No. 536-F(PEN) dated 01.10.2019 for more information.
## Other Changes:
Latest release includes various bug fixes and improvements.
Source code updated with helpful Dicstrings for better understanding.
 
 # How to Install :
  # For Windows OS :
   1. Download the zip archive file for Windows by <a href="https://github.com/loku-sama/pension-calculator/releases/download/1.2.0/Basic_Retirement_Benefits_Calculator_ver_1.2.0.zip"> CLICKING HERE (Latest)</a> and unzip it. 
   2. Run the Basic_Retirement_Benefit_Calculator.exe (windows executable) file, no need to install the app.
  # For Linux OS :
    Coming Soon.
 
 # Features :
 1. This is an Offline application, so no need of an Internet connection.
 2. Basic Pension, Family Pension, Commuted Value of Pension, Gratuity (Retiring and Death) and Leave Salary Calculators in one application.
 3. Easy to use, just input required data and click on calculate button. Also you can generate reports and print them.
 4. Updated on the basis of the latest Govt. rules and orders (ROPA 2019).
 5. This application is completely free and open source.

# Important :
If you are a regular user, just download the .zip file, extract it and run .exe file to use the application. No need to install it.
If you want to check the source code and want to build something better, please download the benefit_calculator_ver-1.0.1.py file or the new source_code_ver_1.2.0 files and run the 'main.py' along with its dependencies.
For any suggestions or Bug reporting, please contact me at happysourav96@gmail.com

# Screenshots :
<img src="https://sourceforge.net/p/pension-calculator/screenshot/new home.PNG" alt="hom" height="400px" width="400px">      <img src="https://sourceforge.net/p/pension-calculator/screenshot/gra.PNG" alt="gratuity-calculator" height="400px" width="400px">
<img src="https://sourceforge.net/p/pension-calculator/screenshot/pension_new.PNG" alt="pension-calculator" height="400px" width="400px">  <img src="https://sourceforge.net/p/pension-calculator/screenshot/leave.PNG" alt="pension-calculator" height="400px" width="400px">

# How to Run the Source Code :
1. First download all the source_code_ver_1.2.0 files (including the requirements.txt file) and install python3 if you dont have it.
2. Run the following command in your terminal to install all the required dependencies at once.
  ```python
  pip install requirements.txt
  ```
3. Now go to the parent folder and open terminal there. You must put the 'templates' folder in the parant directory.
4. Move all the files from assets folder into the main directory.
5. Now run the following command -
```python
python main.py
```

# Contribuion :
If you're new to contributing to Open Source on Github, <a href="https://guides.github.com/activities/contributing-to-open-source/">this guide</a> can help you get started. 
