"""
 #############################################   READ ME   ############################################
 # A simple retirement benefit calculator app written in Python and for GUI I used PySimpleGUI module #
 # This application is open source under GNU License v.3.                                             #
 # For any feedback or bug reporting, contact me at github - https://github.com/loku-sama             #
 # Author : SOURAV (Loku), A newbie coder.                                                            #
 # Dependencies needed to run the code : 1. Python3                                                   #
 #                                2. PySimpleGUI module                                               #
 #                                3. Dateutil module                                                  #
 #                                4. Default datetime module (optional)                               #
 ######################################################################################################
"""

# Start of Import section
import PySimpleGUI as sg
from datetime import datetime
from dateutil import relativedelta

# Application main theme
sg.theme("BlueMono")
format_date = "%d/%m/%Y"

# Main menu layout start
menu_def = [
    ['File       ',
     [
         'Home',
         '---',
         'Pension Calculator',
         '---',
         "Gratuity Calculator",
         '---',
         "Leave Salary Calculator",
         "---",
         'Exit'
     ],
     ],
    ['Help       ',
     [
         'Rules and Orders',
         '---',
         'About',
         '---',
         'Fork Me on Github',
         '---',
         'Check for Updates',
     ]
     ]
]

# App home page layout
home_layout = [
    [sg.Text("Basic Retirement Benefits Calculator ( As per ROPA 2019)", size=(700, 3), justification="center",
             font=(20))],
    [sg.Text("", size=(27, 5)), sg.Button("Pension", size=(30, 3), key="pen", )],
    [sg.Text("", size=(27, 5)), sg.Button("Gratuity", size=(30, 3), key="gra")],
    [sg.Text("", size=(27, 5)), sg.Button("Leave Salary", size=(30, 3), key="leave")],
    [sg.HSeparator()],
    [sg.Text("How to use :", font=(0.5), size=(67, 1)), sg.Button(button_text="Source Code", key="git",
                                                                  tooltip="Click here to check the source code.")],
    [sg.Text("1. This is an OFFLINE app, so no need of Internet Connection. Just select any type of calculator from the"
             " main menu.\n2. Enter valid data in the given input fields and click CALCULATE button." 
             "\n3. Check your results in the output "
             "fields, As simple as that. More features will be added in future releases.")],
    [sg.Text("Notice :", font=(0.5))],
    [sg.Text("This is a complete free and open source project."), sg.Text("Free-Software-movement (Click Here)",
                                                                          size=(40, 1), key="fsm",
                                                                          tooltip="Click here to know more.",
                                                                          font=("u"), enable_events=True),
     ]
]

# Global username layout
user_name_pen = [
    [sg.HSeparator()],
    [
        sg.Text("Name: ", size=(5, 1)),
        sg.InputText(size=(38, 1), enable_events=True, key="name", border_width=2),
        sg.Button("Submit"),
        sg.VSeparator(),
        sg.Text("Welcome: ", size=(8, 1)),
        sg.In(key="display_name", size=(40, 1), disabled=True, border_width=2, default_text="User_Name")
    ],
    [sg.HSeparator()]
]

# Pension calculator layout
head_pension = [
    [sg.Text("Basic Pension Calculator (ROPA 2019)", size=(700, 1), justification="center", font=(15))],
    [sg.HSeparator()],
]
first_column_pen = [
    [
        sg.Text("Date of Joining:\n(DD/MM/YYYY) "),
        sg.Text(size=(7, 3)),
        sg.Input("", key="dojPick", size=(15, 1), enable_events=False, disabled=False, border_width=2, ),
        sg.CalendarButton(title="Date of Joining", key="doj", enable_events=False, disabled=False, format=format_date,
                          no_titlebar=False, button_text="Choose Date")
    ],
    [
        sg.Text("Date of Retirement:\n(DD/MM/YYYY)  "),
        sg.Text(size=(5, 1)),
        sg.Input("", key="dorPick", size=(15, 1), enable_events=False, disabled=False, border_width=2, ),
        sg.CalendarButton("Choose Date", key="dor", enable_events=False, disabled=False, format=format_date,
                          no_titlebar=False),
    ],
    [
        sg.Text("Last Basic Pay:"),
        sg.Text(size=(7, 3)),
        sg.Input(key="basic", size=(28, 3), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Minimum basic pay is Rs.17000", ),
    ],
    [
        sg.Text("Other Allowances (NPA) :\n(If any) ", size=(20, 2)),
        sg.Input(key="npa1", size=(28, 2), disabled=False, default_text=int(0), border_width=2)
    ],
    [
        sg.Text("Percentage of \nCommutation:"),
        sg.Text(size=(8, 2)),
        sg.Input(key="comm", size=(28, 1), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Maximum commutation is 40%", ),
    ],
    [sg.Text("", size=(0, 2))],
    [
        sg.Text("", size=(12, 1)),
        sg.Button("CALCULATE", tooltip="Click to calculate pension.", focus=True, size=(20, 1)),
    ],
]
second_column_pen = [
    [sg.Text("Last Pay Drawn (Basic+Other) : ", size=(25, 1))],
    [sg.Input(" ", size=(35, 2), disabled=True, key="total-pay-pen")],
    [
        sg.Text("Qualifying Years of Service : "),
    ],
    [sg.In("", key="q_service", size=(35, 1), disabled=True, border_width=2, )],
    [sg.Text("Qualifying Service in 6 monthly units : \n(Max 40 units) ", size=(30, 2))],
    [sg.In("", key="xx", size=(35, 1), disabled=True, border_width=2, )],
    [
        sg.Text("Basic Pension:\n(Rounded Off)", size=(15, 2), ),
        sg.Input("0", key="Bpen", size=(16, 1), disabled=True, border_width=2, )
    ],
    [
        sg.Text("Reduced Pension:\n(Rounded Off)", size=(15, 2), ),
        sg.Input("0", key="Rpen", size=(16, 1), disabled=True, border_width=2, )
    ],
    [
        sg.Text("Family Pension:\n(Rounded Off)", size=(15, 2), ),
        sg.Input("0", key="Fpen", size=(16, 1), disabled=True, border_width=2, )
    ],
]
footer_pen = [
    [sg.HSeparator()],
    [sg.Text("Important Notes: ", font=(1))],
    [sg.Text("1. Basic pension can not exceed Rs. 100500.00 and minimum Basic Pension is Rs. 8500.00")],
    [sg.Text(
        "2. Minimum qualifying service period to get pension is 10 years (Not applicable in case of Family Pension).")],
    [sg.Text(
        "3. Six Monthly installment of qualifying service is limited to 40 units even if qualifying service period is "
        "more than 20 years.\n    For more information please refer WB DCRB Rules 1971 and ROPA 2019.")],
]
layout_pension = [
    [sg.Column(head_pension, visible=True)],
    [
        sg.Column(first_column_pen, visible=True, key="pen_entry"),
        sg.VSeparator(),
        sg.Column(second_column_pen, visible=True, key="pen_result"),
    ],
    [sg.Column(footer_pen, visible=True, key="pen_footer")],
]

# Gratuity calculator Layout start
head_gra = [
    [sg.Text("Gratuity Calculator (ROPA 2019)", size=(700, 1), justification="center", font=(15))],
    [sg.HSeparator()],
]
gra_first_column = [
    [
        sg.Text("Date of Joining:\n(DD/MM/YYYY) "),
        sg.Text(size=(7, 3)),
        sg.Input("", key="dojPick1", size=(15, 1), enable_events=False, disabled=False, border_width=2),
        sg.CalendarButton(title="Date of Joining", key="doj1", enable_events=False, disabled=False, format=format_date,
                          no_titlebar=False, button_text="Choose Date")
    ],
    [
        sg.Text("Date of Retirement:\n(DD/MM/YYYY)  "),
        sg.Text(size=(5, 1)),
        sg.Input("", key="dorPick1", size=(15, 1), enable_events=False, disabled=False, border_width=2, ),
        sg.CalendarButton(title="Date of Retirement", key="dor1", enable_events=False, disabled=False,
                          format=format_date,
                          no_titlebar=False, button_text="Choose Date"),
    ],
    [
        sg.Text("Last Basic Pay:"),
        sg.Text(size=(7, 3)),
        sg.Input(key="basic1", size=(28, 3), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Minimum basic pay is Rs.17000"),
    ],
    [
        sg.Text("DA:\n(If any) ", size=(20, 2)),
        sg.Input(key="da", size=(28, 2), disabled=False, default_text=int(0), border_width=2)
    ],
    [
        sg.Text("Other Allowances (NPA):\n(If any) ", size=(20, 2)),
        sg.Input(key="npa", size=(28, 2), disabled=False, default_text=int(0), border_width=2)
    ],
    [
        sg.Text("", size=(0, 2)),
    ],
    [
        sg.Text("", size=(15, 1)),
        sg.Button("CALCULATE", key="cal_gra", tooltip="Click to calculate Gratuity.", focus=True, size=(20, 1)),
    ],
]
gra_second_col = [
    [sg.Text("Last Pay Drawn (Basic+DA+Other) : ", size=(28, 1))],
    [sg.Input(" ", size=(35, 2), disabled=True, key="total-pay-gra")],
    [sg.Text("Qualifying Years of Service : ")],
    [sg.In("", key="q_service1", size=(35, 1), disabled=True, border_width=2)],
    [sg.Text("Qualifying Service in 6 monthly units : \n(Max 66 units) ", size=(30, 2))],
    [sg.In("", key="xx1", size=(35, 1), disabled=True, border_width=2)],
    [
        sg.Text("Retiring Gratuity:\n(Rounded Off)", size=(15, 2), ),
        sg.Input("0", key="Rgra", size=(16, 1), disabled=True, border_width=2)
    ],
    [
        sg.Text("Death Gratuity:\n(Rounded Off)", size=(15, 2), ),
        sg.Input("0", key="Dgra", size=(16, 1), disabled=True, border_width=2)
    ],
]

gra_footer = [
    [sg.HSeparator()],
    [sg.Text("Important Notes: ", font=(1))],
    [sg.Text("1. Maximum amount of Death/Retiring Gratuity is Rs.12,00,000.00. [Only applicable on and from "
             "01.01.2016].")],
    [sg.Text(
        "2. Emoluments for calculating Gratuity includes basic pay, DA, Non Practicing Allowance (if any). ")],
    [sg.Text(
        "3. Six Monthly installment of qualifying service is limited to 66 units even if qualifying service period is "
        "more than 33 years.\n    For more information please refer WB DCRB Rules 1971 and ROPA 2019.")]
]

gra_layout = [
    [sg.Column(head_gra, visible=True)],
    [sg.Column(gra_first_column, visible=True, ),
     sg.VSeparator(),
     sg.Column(gra_second_col, visible=True)],
    [sg.Column(gra_footer, visible=True)]
]

# Leave salary calculator layout
head_leave = [
    [sg.Text("Leave Salary Calculator (ROPA 2019)", size=(700, 1), justification="center", font=(15))],
    [sg.HSeparator()],
]
leave_first_column = [
    [
        sg.Text("Leave Due At Credit as on Retirement\nOr Death(Not greater than 300):"),
        sg.Text(size=(5, 3)),
        sg.Input(key="leave-due", size=(12, 3), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Maximum leave due must not exceed 300 days."),
    ],
    [
        sg.Text("Last Basic Pay:"),
        sg.Text(size=(7, 3)),
        sg.Input(key="basic2", size=(28, 3), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Minimum basic pay is Rs.17000"),
    ],
    [
        sg.Text("DA:\n(If any) ", size=(20, 2)),
        sg.Input(key="da1", size=(28, 2), disabled=False, default_text=int(0), border_width=2)
    ],
    [
        sg.Text("Do you enrolled under WBHS 2008?", size=(20, 2)),
        sg.Radio(text="Yes", enable_events=True, key="wbhs-yes", group_id="ma", default=True, ),
        sg.Radio(text="No", enable_events=True, key="wbhs-no", group_id="ma", ),
    ],
    [
        sg.Text("Medical Allowance:  ", size=(20, 1)),
        sg.Input(key="ma", size=(28, 2), disabled=True, default_text=int(0), border_width=2)
    ],
    [
        sg.Text("", size=(0, 0)),
    ],
    [
        sg.Text("", size=(15, 1)),
        sg.Button("CALCULATE", key="cal_leave", tooltip="Click to calculate Leave Salary.", focus=True, size=(20, 1)),
    ],
]
leave_second_column = [
    [sg.Text("Last Pay Drawn (Basic+DA+MA) : ", size=(25, 2))],
    [sg.Input(" ", size=(45, 2), disabled=True, key="total-pay")],
    [sg.Text("Total Leave Salary : ", size=(25, 2))],
    [sg.Input(" ", size=(45, 2), disabled=True, key="leave-sal")],
]
leave_footer = [
    [sg.HSeparator()],
    [sg.Text("Important Notes : ", font=(1))],
    [sg.Text("1. After retirement or death of a Government Employee his/her utilized earned leaves may be encashed up "
             "to 300 days.")],
    [sg.Text(
        "2. Leave salary calculation should be done on the basis of last month's pay of the employee.")],
    [sg.Text(
        "3. In case an employee resigns or quits from service, he will be granted leave encashment for a period not "
        "exceeding\n    half the E.L. due subject to maximum limit not exceeding 150 days.")],
    [sg.Text("4. Leave due includes- i. Earned Leave, ii. Half Pay Leave, iii. Commuted Leave, iv. Leave not due, v. "
             "Extraordinary\n    Leave. Please refer "
             "Rule 168A, 168B & 168C of W.B.S.R. Part-I for more information.")]
]

leave_calculator_layout = [
    [sg.Column(head_leave, visible=True)],
    [sg.Column(leave_first_column, visible=True),
     sg.VSeparator(),
     sg.Column(leave_second_column, visible=True),
     ],
    [sg.Column(leave_footer, visible=True)]
]

# Main app layout
main_layout = [
    [sg.Menu(menu_def, tearoff=False, key="menu")],
    [sg.Column(user_name_pen, key="username", visible=True)],
    [sg.Column(home_layout, key='home', visible=True), sg.Column(layout_pension, key="pen_display", visible=False),
     sg.Column(gra_layout, key="gra_display", visible=False),
     sg.Column(leave_calculator_layout, key="leave_cal", visible=False)],
]
window = sg.Window("Basic Retirement Benefits  for employees of WB Govt. (Offline Application)", main_layout, size=(755, 600),
                   resizable=False,
                   icon=r'icon.ico', )
new_menu_def = menu_def

# Start of main loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break  # Breaks the main loop if the user closes the window

    if event == 'Home':
        window['pen_display'].update(visible=False)
        window['gra_display'].update(visible=False)
        window['leave_cal'].update(visible=False)
        window['home'].update(visible=True)
    if event == "pen" or event == "Pension Calculator":
        window['pen_display'].update(visible=True)
        window['gra_display'].update(visible=False)
        window['leave_cal'].update(visible=False)
        window['home'].update(visible=False)
    if event == "gra" or event == "Gratuity Calculator":
        window['gra_display'].update(visible=True)
        window['pen_display'].update(visible=False)
        window['leave_cal'].update(visible=False)
        window['home'].update(visible=False)
    if event == "leave" or event == "Leave Salary Calculator":
        window['leave_cal'].update(visible=True)
        window['gra_display'].update(visible=False)
        window['pen_display'].update(visible=False)
        window['home'].update(visible=False)
    if event == "git":
        sg.webbrowser.open(url='https://github.com/loku-sama/pension-calculator', new=2)
    if event == "fsm":
        sg.Popup("The free software movement is a social movement with the goal of obtaining and guaranteeing certain "
                 "freedoms for software users, namely the freedom to run the software, to study the software, "
                 "to modify the software, to share possibly modified copies of the software. Software which "
                 "meets these requirements is termed free software. The word 'free' is ambiguous in English, "
                 "although in this context, it means 'free as in freedom', not 'free as in zero price'."
                 "\nSource: Wikipedia", title="Free "
                                              "Software Movement", custom_text="Close",
                 icon=r'icon.ico', )
        if event == 'ok':
            sg.webbrowser.open(url='https://en.wikipedia.org/wiki/Free_software_movement', new=2)

    if event == "Submit":
        name = values['name']
        if name is not None:
            window["display_name"].update(name)
        else:
            sg.Popup("Please Enter Your Name.")

    if event == "About":
        sg.Popup("Basic Retirement Benefits Calculator for employees of Govt. of West Bengal.\nVersion - 1.0.1\n"
                 "App coded by SOURAV, Language- Python.\nApp programmed on the basis of latest Govt. rules and Orders."
                 "\nThis is for informational purpose only. Please refer original Rules and Orders thoroughly.\n"
                 "This application is Open Source and licensed under GNU Public License V.3. You can download the"
                 " source code from Github. \nThis app will get updated in case of any change in rules and orders. "
                 " Always download the latest release from the Github page.",
                 title="About",
                 icon=r'icon.ico', )
    if event == 'Fork Me on Github':
        sg.webbrowser.open(url='https://github.com/loku-sama', new=2, )
    if event == 'Check for Updates':
        sg.webbrowser.open(url='https://github.com/loku-sama/pension-calculator/releases/', new=2, )
    if event == 'Rules and Orders':
        sg.webbrowser.open(url='http://www.wbfin.nic.in/New_Fin/Pages/Publication.aspx', new=2, )

    format_new = "%d/%m/%Y"
    qua_service_in_months = 0
    commutation = 0
    pension = 0
    basic_pension = 0
    family_pension = 0

    if event == "CALCULATE":
        try:
            doa = datetime.strptime(values["dojPick"], format_new)
            dor = datetime.strptime(values["dorPick"], format_new)
            diff = relativedelta.relativedelta(dor, doa)
            year = diff.years
            mon = diff.months
            days = diff.days
            six_monthly_installament = year * 2
            qua_service_in_months = 0
            basic_pay = int(values['basic'])
            npa = int(values['npa1'])
            total_pay = basic_pay + npa


            def qualifying_ins_calculation():
                """ Function for calculating the net qualifying service period in 6 monthly installments. """
                global qua_service_in_months, mon
                if (mon >= 3) and (mon < 6):
                    qua_service_in_months = six_monthly_installament + 1
                elif (mon >= 6) and (mon < 9):
                    qua_service_in_months = six_monthly_installament + 1
                elif (mon >= 9) and (mon < 12):
                    qua_service_in_months = six_monthly_installament + 2
                else:
                    qua_service_in_months = six_monthly_installament
                return qua_service_in_months


            def check_basic_pay(n):
                """ Function for checking the minimum basic pay as per ROPA 2019. """
                global basic_pay
                if n < 17000:
                    sg.Popup("Basic Pay can not be less than Rs.17000 as per ROPA 2019", title="Error!",
                             icon=r'icon.ico')
                elif n >= 17000:
                    n = basic_pay
                return n

            check_basic_pay(basic_pay)
            window['total-pay-pen'].update(total_pay)
            window['q_service'].update("{} years {} months".format(year, mon))

            if year < 10:
                qualifying_ins_calculation()
                window['xx'].update(qua_service_in_months)
                family_pension = round((total_pay * 30) / 100)
                sg.Popup("Sorry! You are not eligible for Regular Pension.", title="Error!",
                         icon=r'icon.ico')
            elif year > 20:
                qua_service_in_months = 40
                window['xx'].update(qua_service_in_months)
            else:
                qualifying_ins_calculation()
                window['xx'].update(qua_service_in_months)


            def check_commutation():
                """ Function for checking the pension commutation limits as per ROPA 2019. """
                global commutation
                com = int(values['comm'])
                if com > 40:
                    sg.Popup("Commutation must not exceed 40%. Try again.", title="Error!",
                             icon=r'icon.ico')
                    commutation = 100
                else:
                    commutation = com
                return commutation

            check_commutation()


            def get_pension(a, b):
                """ Function for calculating basic pension. """
                global pension
                global basic_pension
                if 20 < qua_service_in_months < 40 and commutation <= 40:
                    basic_pension = ((a / 2) * qua_service_in_months) / 40
                elif qua_service_in_months >= 40 and commutation <= 40:
                    basic_pension = a / 2
                elif qua_service_in_months > 20 and commutation > 40:
                    basic_pension = ((a / 2) * qua_service_in_months) / 40
                elif qua_service_in_months >= 40 and commutation > 40:
                    basic_pension = a / 2
                return basic_pension

            get_pension(total_pay, commutation)


            def determine_basic_pension(pen):
                """ Function for calculating minimum and maximum pension limit. """
                if pen < 8500 and year >= 10 and basic_pay >= 17000:
                    bpen = 8500
                elif pen > 100500 and year >= 10 and basic_pay >= 17000:
                    bpen = 100500
                elif year >= 10 and basic_pay >= 17000:
                    bpen = pen
                else:
                    bpen = 0
                return round(bpen)

            window['Bpen'].update(round(determine_basic_pension(basic_pension)))
            final_basic_pension = determine_basic_pension(basic_pension)


            def determine_reduced_pension(pen, com):
                """ Function for calculating reduced basic pension. """
                global pension
                if com == 0:
                    pension = round(pen)
                elif 1 <= com <= 40:
                    pension = round(pen - (pen * com / 100))
                elif com > 40:
                    pension = "Error! Commutation must not exceed 40%."
                return pension

            window['Rpen'].update(determine_reduced_pension(final_basic_pension, commutation))


            def get_family_pension(pay):
                """ Function for calculating Family pension. """
                global family_pension
                if basic_pay >= 17000 and (year < 10 or year >= 10):
                    family_pension = pay * 30 / 100
                    if family_pension < 8500:
                        family_pension = 8500
                    elif family_pension > 60300:
                        family_pension = 60300
                    elif family_pension > final_basic_pension:
                        family_pension = final_basic_pension
                if basic_pay >= 17000 and (year < 10 or year >= 10):
                    family_pension = pay * 30 / 100
                    if family_pension < 8500:
                        family_pension = 8500
                    elif family_pension > 60300:
                        family_pension = 60300
                else:
                    family_pension = 0
                return round(family_pension)

            window['Fpen'].update(get_family_pension(total_pay))
        except:
            sg.Popup("Please enter values in proper format.\n Ex- Dates in DD/MM/YYYY Format", title="Error!",
                     icon=r'icon.ico')

    # Start of Gratuity calculator Functions:
    if event == "cal_gra":
        try:
            doa = datetime.strptime(values["dojPick1"], format_new)
            dor = datetime.strptime(values["dorPick1"], format_new)
            diff = relativedelta.relativedelta(dor, doa)
            year = diff.years
            mon = diff.months
            days = diff.days
            six_monthly_installment = year * 2
            basic_pay = int(values['basic1'])
            da = int(values['da'])
            oth = int(values['npa'])
            total_pay = basic_pay + da + oth
            qua_service_in_months_gra = 0
            death_gratuity = 0
            retiring_gratuity = 0


            def qualifying_ins_calculation_gratuity():
                """ Function for calculating the net qualifying service period in 6 monthly installments. """
                global qua_service_in_months_gra
                if (mon >= 3) and (mon < 6):
                    qua_service_in_months_gra = six_monthly_installment + 1
                elif (mon >= 6) and (mon < 9):
                    qua_service_in_months_gra = six_monthly_installment + 1
                elif (mon >= 9) and (mon < 12):
                    qua_service_in_months_gra = six_monthly_installment + 2
                else:
                    qua_service_in_months_gra = six_monthly_installment
                return qua_service_in_months_gra


            def check_basic_pay(n):
                """ Function for checking minimum basic pay as per ROPA 2019. """
                global basic_pay
                if n < 17000:
                    sg.Popup("Basic Pay can not be less than Rs.17000 as per ROPA 2019", title="Error!",
                             icon=r'icon.ico')
                elif n >= 17000:
                    n = basic_pay
                return n

            check_basic_pay(basic_pay)
            window['total-pay-gra'].update(total_pay)
            window['q_service1'].update("{} years {} months".format(year, mon))
            if year >= 33:
                qua_service_in_months_gra = 66
                window['xx1'].update(qua_service_in_months_gra)
            else:
                qualifying_ins_calculation_gratuity()
                window['xx1'].update(qua_service_in_months_gra)


            def get_retiring_gratuity(y, tp):
                """ Function for calculating the retiring Gratuity amount. """
                global retiring_gratuity
                if y < 10 and basic_pay >= 17000:
                    retiring_gratuity = round((tp * qua_service_in_months_gra) / 2)
                elif y >= 10 and basic_pay >= 17000:
                    retiring_gratuity = round((tp * qua_service_in_months_gra) / 4)
                else:
                    retiring_gratuity = 0
                return round(retiring_gratuity)

            get_retiring_gratuity(year, total_pay)


            def get_death_gratuity(y, tp):
                """ Function for calculating the death Gratuity amount. """
                global death_gratuity
                if y < 1 and basic_pay >= 17000:
                    death_gratuity = 2 * tp
                elif 1 <= y < 5 and basic_pay >= 17000:
                    death_gratuity = 6 * tp
                elif 5 <= y < 11 and basic_pay >= 17000:
                    death_gratuity = 12 * tp
                elif 11 <= y < 20 and basic_pay >= 17000:
                    death_gratuity = 20 * tp
                elif y >= 20 and basic_pay >= 17000:
                    death_gratuity = (tp * qua_service_in_months_gra) / 2
                else:
                    death_gratuity = 0
                return round(death_gratuity)

            get_death_gratuity(year, total_pay)


            def check_gratuity(gra):
                """ Function for checking maximum limit of Gratuity amount as per ROPA 2019. """
                if gra > 1200000:
                    gra = 1200000
                return gra

            window['Rgra'].update(check_gratuity(retiring_gratuity))
            window['Dgra'].update(check_gratuity(death_gratuity))

        except:
            sg.Popup("Please enter values in proper format.\n Ex- Dates in DD/MM/YYYY Format", title="Error!",
                     icon=r'icon.ico')

    if event == "wbhs-no":
        ma = 500
        window["ma"].update(ma)
        window.refresh()
    else:
        ma = 0
        window["ma"].update(ma)
        window.refresh()
    if event == "cal_leave":
        try:
            basic_pay = int(values['basic2'])
            da = int(values['da1'])
            ma = int(values['ma'])
            total_pay = basic_pay + da + ma
            leave_due = int(values['leave-due'])
            leave_salary = 0


            def check_basic_pay(n):
                """ Function for checking minimum basic pay as per ROPA 2019. """
                global basic_pay
                if n < 17000:
                    sg.Popup("Basic Pay can not be less than Rs.17000 as per ROPA 2019", title="Error!",
                             icon=r'icon.ico')
                elif n >= 17000:
                    n = basic_pay
                return n

            check_basic_pay(basic_pay)

            if values['wbhs-no']:
                ma = 500
                window["ma"].update(ma)
                window.refresh()
            else:
                ma = 0
                window["ma"].update(ma)
                window.refresh()
            window['total-pay'].update(total_pay)


            def calculate_leave_salary(tp, leave):
                """ Function for calculating leave salary amount. """
                global leave_salary, leave_due
                if leave_due > 300:
                    sg.Popup("Maximum leave due can not exceed 300 days.", title="Error!",
                             icon=r'icon.ico')
                    window['leave-sal'].update("Error! Leave due exceeds 300 days. Try again.")
                elif leave_due <= 300 and basic_pay >= 17000:
                    leave_salary = round((tp * leave) / 30)
                    window['leave-sal'].update(leave_salary)
                else:
                    leave_salary = 0
                    window['leave-sal'].update(leave_salary)
                return leave_salary

            calculate_leave_salary(total_pay, leave_due)
        except:
            sg.Popup("Please enter values in proper format.", title="Error!",
                     icon=r'icon.ico')
window.close()  # Closes the main window if loop ends.
