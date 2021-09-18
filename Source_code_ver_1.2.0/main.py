"""
 #############################################   READ ME   ############################################
 # A simple retirement benefit calculator app written in Python and for GUI I used PySimpleGUI module #
 # This application is open source under GNU License v.3.                                             #
 # For any feedback or bug reporting, contact me at github - https://github.com/loku-sama             #
 # Author : SOURAV (Loku), A newbie coder.                                                            #
 # Dependencies to run the code : 1. Python3                                                          #
 #                                2. PySimpleGUI module                                               #
 #                                3. Dateutil module                                                  #
 #                                4. Default datetime, requests, os module                            #
 #                                5. jinja2 module to generate HTML reports                           #
 ######################################################################################################
"""
import layout
import pension
import gratuity
import leave_salary
import feedback
from datetime import datetime
import requests

# Info of current version
curr_x = 1
curr_y = 2
curr_z = 0


def check_update():
    """  Function to check the app Updates

    :return: True or False
    :rtype: bool
    """
    try:
        response = requests.get("https://api.github.com/repos/loku-sama/pension-calculator/releases/latest")
        # Getting the latest release version from GitHub API
        github_version = str(response.json()["tag_name"])  # Processing the JSON file
        x = github_version[0:1]  # Slicing the string
        y = github_version[2:3]
        z = github_version[4:5]
        if int(x) > curr_x or int(y) > curr_y or int(z) > curr_z:
            update = layout.sg.popup_yes_no("Good News! An Updated version is available.\n"
                                            "Do you want to update now to use the latest features?\n"
                                            "(You can delete the old version after the update)", title="Update Now?",
                                            icon=r'icon.ico')
            if update == 'Yes':
                layout.sg.webbrowser.open(url='https://github.com/loku-sama/pension-calculator/releases/latest', new=2)
            return True
        else:
            return False
    except:
        pass


check_update()

while True:
    event, values = layout.window.read()

    if event in ["Exit", layout.sg.WIN_CLOSE_ATTEMPTED_EVENT]:
        confirm = layout.sg.popup_yes_no("Do you really want to close the Application?", title="Confirm Exit?",
                                         icon=r'icon.ico', text_color="red")
        if confirm == 'Yes':
            break  # Breaks the main loop if the user clicks Yes button

    if event == 'Home':
        layout.window['username'].update(visible=True)
        layout.window['pen_display'].update(visible=False)
        layout.window['gra_display'].update(visible=False)
        layout.window['leave_cal'].update(visible=False)
        layout.window['home'].update(visible=True)
        layout.window['feedback_layout'].update(visible=False)

    if event in ["pen", "Pension Calculator"]:
        layout.window['username'].update(visible=True)
        layout.window['pen_display'].update(visible=True)
        layout.window['gra_display'].update(visible=False)
        layout.window['leave_cal'].update(visible=False)
        layout.window['home'].update(visible=False)
        layout.window['feedback_layout'].update(visible=False)

    if event in ["gra", "Gratuity Calculator"]:
        layout.window['username'].update(visible=True)
        layout.window['gra_display'].update(visible=True)
        layout.window['pen_display'].update(visible=False)
        layout.window['leave_cal'].update(visible=False)
        layout.window['home'].update(visible=False)
        layout.window['feedback_layout'].update(visible=False)

    if event in ["leave", "Leave Salary Calculator"]:
        layout.window['username'].update(visible=True)
        layout.window['leave_cal'].update(visible=True)
        layout.window['gra_display'].update(visible=False)
        layout.window['pen_display'].update(visible=False)
        layout.window['home'].update(visible=False)
        layout.window['feedback_layout'].update(visible=False)

    if event == "git":
        layout.sg.webbrowser.open(url='https://github.com/loku-sama/pension-calculator', new=2)

    if event == "fsm":
        con = layout.sg.popup(
            "The free software movement is a social movement with the goal of obtaining and "
            "guaranteeing certain "
            "freedoms for software users, namely the freedom to run the software, to study the software, "
            "to modify the software, to share possibly modified copies of the software. Software which "
            "meets these requirements is termed free software. The word 'free' is ambiguous in English, "
            "although in this context, it means 'free as in freedom', not 'free as in zero price'."
            "\nSource: Wikipedia", title="Free Software Movement", icon=r'icon.ico', custom_text="Know More")
        if con == "Know More":
            layout.sg.webbrowser.open(url='https://en.wikipedia.org/wiki/Free_software_movement', new=2)

    if event == "Submit":
        name = str(values['display_name'])
        if name != "User_Name" or values['name'] != "":
            layout.window["display_name"].update(values['name'])
        else:
            layout.sg.Popup("Please Enter a valid Name!", title="Error!", icon=r'icon.ico')

    if event == "About the App":
        layout.sg.popup("Basic Retirement Benefits Calculator for employees of Govt. of West Bengal.\nVersion - 1.2.0\n"
                        "App coded by SOURAV, Language- Python and a little HTML."
                        "\nApp programmed on the basis of latest Govt. rules and Orders."
                        "\nThis is for informational purpose only. Please refer original Rules and Orders thoroughly.\n"
                        "This application is Open Source and licensed under GNU Public License V.3. You can download "
                        "the source code from Github. \nThis app will get updated in case of any change in rules and "
                        "orders. Always download the latest release from the Github page.", title="About the Application",
                        icon=r'icon.ico', )
    if event == 'Fork Me on Github':
        layout.sg.webbrowser.open(url='https://github.com/loku-sama', new=2, )

    if event == 'Check for Updates':
        internet = feedback.connect()
        if internet:
            up = check_update()
            if not up:
                layout.sg.popup("Your version is up to date! We will let you know when an update is available.",
                                title="Congrats!", icon=r'icon.ico')
        else:
            layout.sg.popup("Please check your Internet connection and try again", title="Error!", icon=r'icon.ico')

    if event == 'Rules and Orders':
        layout.sg.webbrowser.open(url='http://www.wbfin.nic.in/New_Fin/Pages/Publication.aspx', new=2, )

    if event == 'gnu':
        layout.sg.webbrowser.open(url='https://www.gnu.org/gnu/linux-and-gnu.html', new=2, )

    if event == 'python':
        layout.sg.webbrowser.open(url='https://www.python.org/', new=2, )

    if event == "Contact Me":
        layout.window['leave_cal'].update(visible=False)
        layout.window['gra_display'].update(visible=False)
        layout.window['pen_display'].update(visible=False)
        layout.window['home'].update(visible=False)
        layout.window['username'].update(visible=False)
        layout.window['feedback_layout'].update(visible=True)

    if event == "feedback_ok":
        if values['feedback_name'] != "" and values['feedback_email'] != "" and \
                values['feedback_body'] != "":
            true_mail = feedback.check_mail(str(values['feedback_email']))
            if true_mail:
                internet = feedback.connect()
                if internet:
                    try:
                        feed_back = feedback.Feedback("loku-sama@outlook.com", "pa&ao@t1")
                        result = feed_back.send_feedback(values['feedback_name'], values['feedback_email'],
                                                         values['feedback_body'])
                        if result:
                            layout.window['validate'].update("Successful!")
                            layout.sg.popup("Your feedback sent successfully", title="Success!", icon=r'icon.ico')
                        else:
                            layout.window['validate'].update("Error!")
                            layout.sg.popup("Somethings went wrong! Please try again.", title="Error!",
                                            icon=r'icon.ico')
                    except:
                        layout.sg.popup("Please enter all the required fields.", title="Error!", icon=r'icon.ico')
                else:
                    layout.sg.popup("Please check your Internet connection and try again", title="Error!",
                                    icon=r'icon.ico')
            else:
                layout.sg.popup("Please enter a valid email address and try again", title="Error!", icon=r'icon.ico')
        else:
            layout.sg.popup("Please enter all the required fields.", title="Error!", icon=r'icon.ico')

    if event == "feedback_can":
        layout.window['feedback_layout'].update(visible=False)
        layout.window['home'].update(visible=True)
        layout.window['username'].update(visible=True)

    if event == "CALCULATE":
        try:
            pension.pension_calculation_main(datetime.strptime(values["dojPick"], layout.format_date),
                                             datetime.strptime(values["dorPick"], layout.format_date),
                                             int(values['basic']), int(values['npa1']), int(values['comm']),
                                             int(values['factor']))
        except:
            layout.sg.Popup("Please enter values in proper format.\n Ex- Dates in DD/MM/YYYY Format", title="Error!",
                            icon=r'icon.ico')
            layout.window['pen_report'].update(disabled=True)

    if event == "pen_report":
        try:
            template_var_pension = {"user_name": values['name'], "bp": values['Bpen'], "rp": values['Rpen'],
                                    "fp": values['Fpen'], "doj": values['dojPick'], "dor": values['dorPick'],
                                    "lp": values['total-pay-pen'], "comm": values['comm'], "qs": values['xx'],
                                    "sp": values['q_service'], "cvp": values['cvp'], "age": values['factor']}
            pension.pension_report(template_var_pension)
        except:
            layout.sg.Popup("Something went horribly wrong. Please try again or report the bug.", title="Error!",
                            icon=r'icon.ico')

    if event == "cal_gra":
        try:
            gratuity.gratuity_calculation_main(datetime.strptime(values["dojPick1"], layout.format_date),
                                               datetime.strptime(values["dorPick1"], layout.format_date),
                                               int(values['basic1']), int(values['da']), int(values['npa']))
        except:
            layout.sg.Popup("Please enter values in proper format.\n Ex- Dates in DD/MM/YYYY Format", title="Error!",
                            icon=r'icon.ico')
            layout.window['gra_report'].update(disabled=True)
    if event == "gra_report":
        try:
            template_var_gratuity = {"user_name": values['name'], "rg": values['Rgra'], "dg": values['Dgra'],
                                     "doj": values['dojPick1'], "dor": values['dorPick1'],
                                     "lp": values['total-pay-gra'], "qs": values['xx1'], "sp": values['q_service1']}
            gratuity.gratuity_report(template_var_gratuity)
        except:
            layout.sg.Popup("Something went horribly wrong. Please try again or report the bug.", title="Error!",
                            icon=r'icon.ico')

    if event == "wbhs-no":
        ma = 500
        layout.window["ma"].update(ma)
    else:
        ma = 0
        layout.window["ma"].update(ma)

    if event == "cal_leave":
        try:
            leave_salary.leave_salary_calculation_main(int(values['basic2']), int(values['da1']), int(values['ma']),
                                                       int(values['leave-due']), values['wbhs-no'])
        except:
            layout.sg.Popup("Please enter values in proper format.", title="Error!",
                            icon=r'icon.ico')
            layout.window['leave_report'].update(disabled=True)

    if event == "leave_report":
        try:
            template_var_leave = {"user_name": values['name'], "lp": values['total-pay'], "leave": values['leave-due'],
                                  "leave_sal": values['leave-sal']}
            leave_salary.leave_salary_report(template_var_leave)
        except:
            layout.sg.Popup("Something went horribly wrong. Please try again or report the bug.", title="Error!",
                            icon=r'icon.ico')

layout.window.close()
