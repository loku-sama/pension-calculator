import PySimpleGUI as sg
from jinja2 import Environment, FileSystemLoader
import os
import datetime

sg.theme("BlueMono")  # App main Theme
format_date = "%d/%m/%Y"  # Date format
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # Time stamp to generate dynamic report filename
current_directory = os.getcwd()  # Getting current working directory

# Start of HTML Report Templates section
env = Environment(loader=FileSystemLoader('./templates'))
template_pen = env.get_template("report_tem_pen.html")  # Template file for Pension report
template_gra = env.get_template("report_tem_gra.html")  # Template file for Gratuity report
template_leave = env.get_template("report_tem_leave.html")  # Template file for Leave Salary report

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
         'About the App',
         '---',
         'Contact Me',
         '---',
         'Fork Me on Github',
         '---',
         'Check for Updates',
     ]
     ]
]

# App home page layout
home_layout = [
    [sg.Text("Basic Retirement Benefits Calculator ( As per ROPA 2019)", size=(700, 2), justification="center",
             font=(20)),
     ],
    [sg.Text("", size=(27, 5)), sg.Button("Pension", size=(30, 3), key="pen", )],
    [sg.Text("", size=(27, 5)), sg.Button("Gratuity", size=(30, 3), key="gra")],
    [sg.Text("", size=(27, 5)), sg.Button("Leave Salary", size=(30, 3), key="leave")],
    [sg.HSeparator()],
    [sg.Image(r'python.gif', enable_events=True, key='python', tooltip="Click here to know more!"),
     sg.Text("", size=(60, 1)),
     sg.Image(r'gnu-linux.png', enable_events=True, key='gnu', tooltip="Click here to know more!")
     ],
    [sg.Text("How to use :", font=(0.5), size=(65, 1)), ],
    [sg.Text("1. This is an OFFLINE app, so no need of an Internet Connection. Just select any type of calculator from "
             "the main menu.\n2. Enter valid data in the given input fields and click CALCULATE button."
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
        sg.Input(size=(38, 1), enable_events=True, key="name", border_width=2),
        sg.Button("Submit", key="Submit", enable_events=True),
        sg.VSeparator(),
        sg.Text("Welcome: ", size=(8, 1)),
        sg.Input(key="display_name", size=(40, 1), disabled=True, border_width=2, default_text="User_Name")
    ],
    [sg.HSeparator()]
]

# Pension calculator layout
head_pension = [
    [sg.Text("Basic Pension Calculator (ROPA 2019)", size=(700, 1), justification="center", font=(14))],
    [sg.HSeparator()],
]
first_column_pen = [
    [
        sg.Text("Date of Joining:\n(DD/MM/YYYY) "),
        sg.Text(size=(7, 1)),
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
        sg.Text(size=(7, 2)),
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
    [
        sg.Text("Age as on \nnext Birthday:"),
        sg.Text(size=(8, 2)),
        sg.Input(key="factor", size=(28, 1), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Enter your age as on next Birthday.", ),
    ],
    [sg.Text("", size=(0, 1))],
    [
        sg.Text("", size=(2, 1)),
        sg.Button("CALCULATE", tooltip="Click to calculate pension.", focus=True, size=(20, 1)),
        sg.Button("GENERATE REPORT", tooltip="Click here to generate report", size=(20, 1), disabled=True,
                  key="pen_report")
    ],
]
second_column_pen = [
    [sg.Text("Last Pay Drawn (Basic+Other) : ", size=(25, 1))],
    [sg.Input(" ", size=(35, 2), disabled=True, key="total-pay-pen", border_width=2, )],
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
    [
        sg.Text("Commuted Value of Pension:\n(Rounded Off)", size=(15, 2), ),
        sg.Input("0", key="cvp", size=(16, 1), disabled=True, border_width=2, )
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
        sg.Text("", size=(3, 1)),
        sg.Button("CALCULATE", key="cal_gra", tooltip="Click to calculate Gratuity.", focus=True, size=(20, 1)),
        sg.Button("GENERATE REPORT", tooltip="Click here to generate report", size=(20, 1), disabled=True,
                  key="gra_report")
    ],
]
gra_second_col = [
    [sg.Text("Last Pay Drawn (Basic+DA+Other) : ", size=(28, 1))],
    [sg.Input(" ", size=(35, 2), disabled=True, key="total-pay-gra", border_width=2, )],
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
        "2. Emoluments for calculating Gratuity includes Basic pay, DA, Non Practicing Allowance (if any). ")],
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
    [sg.Text("Leave Due At Credit as on Retirement\nOr Death(Not greater than 300):"), sg.Text(size=(5, 3)),
        sg.Input(key="leave-due", size=(12, 3), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Maximum leave due must not exceed 300 days.")],
    [sg.Text("Last Basic Pay:"), sg.Text(size=(7, 3)),
        sg.Input(key="basic2", size=(28, 3), disabled=False, default_text=int(0), border_width=2,
                 tooltip="Minimum basic pay is Rs.17000")],
    [sg.Text("DA:\n(If any) ", size=(20, 2)),
        sg.Input(key="da1", size=(28, 2), disabled=False, default_text=int(0), border_width=2)],
    [sg.Text("Do you enrolled under WBHS 2008?", size=(20, 2)),
        sg.Radio(text="Yes", enable_events=True, key="wbhs-yes", group_id="ma", default=True, ),
        sg.Radio(text="No", enable_events=True, key="wbhs-no", group_id="ma", )],
    [sg.Text("Medical Allowance:  ", size=(20, 1)),
     sg.Input(key="ma", size=(28, 2), disabled=True, default_text=int(0), border_width=2)],
    [sg.Text("", size=(0, 0)), ],
    [sg.Text("", size=(3, 1)),
     sg.Button("CALCULATE", key="cal_leave", tooltip="Click to calculate Leave Salary.", focus=True, size=(20, 1)),
     sg.Button("GENERATE REPORT", tooltip="Click here to generate PDF report", size=(20, 1), disabled=True,
               key="leave_report")]]

leave_second_column = [
    [sg.Text("Last Pay Drawn (Basic+DA+MA) : ", size=(25, 2))],
    [sg.Input(" ", size=(45, 2), disabled=True, key="total-pay", border_width=2, )],
    [sg.Text("Total Leave Salary : ", size=(25, 2))],
    [sg.Input(" ", size=(45, 2), disabled=True, key="leave-sal", border_width=2, )]]

leave_footer = [
    [sg.HSeparator()],
    [sg.Text("Important Notes : ", font=(1))],
    [sg.Text("1. After retirement or death of a Government Employee, his/her un-utilized earned leaves may be "
             "encashed for a \n    period up to 300 days.")],
    [sg.Text(
        "2. Leave salary calculation should be done on the basis of last month's pay of the employee.")],
    [sg.Text(
        "3. In case an employee resigns or quits from service, he will be granted leave encashment for a period not "
        "exceeding\n    half the E.L. due subject to maximum limit not exceeding 150 days.")],
    [sg.Text("4. Leave due includes- i. Earned Leave, ii. Half Pay Leave, iii. Commuted Leave, iv. Leave not due, v. "
             "Extraordinary\n    Leave. Please refer "
             "Rule 168A, 168B & 168C of W.B.S.R. Part-I for more information.")]]

leave_calculator_layout = [
    [sg.Column(head_leave, visible=True)],
    [sg.Column(leave_first_column, visible=True),
     sg.VSeparator(),
     sg.Column(leave_second_column, visible=True),
     ],
    [sg.Column(leave_footer, visible=True)]]

####################################### Feedback Form Layout #################################################

feedback_layout = [
    [sg.Text("SUBMIT YOUR FEEDBACK", size=(700, 1), font=(15), justification="center")],
    [sg.HSeparator()],
    [sg.Text("Please fill the form below to submit your feedback (An active Internet connection is required)\n Also "
             "you can email me at happysourav96@gmail.com", justification="center", size=(700, 2), )],
    [sg.HSeparator()],
    [sg.Text("", size=(10, 2))],
    [sg.Text("", size=(10, 1)), sg.Text("Your Name * : ", size=(15, 1)), sg.Input(size=(45, 1), key='feedback_name')],
    [sg.Text("", size=(10, 1)), sg.Text("Your Email * : ", size=(15, 1)), sg.Input(size=(45, 1), key='feedback_email')],
    [sg.Text("", size=(10, 1)), sg.Text("Your Feedback * : ", size=(15, 1)), sg.Multiline(size=(45, 15),
     key='feedback_body')],
    [sg.Text("", size=(10, 1), key='validate')],
    [sg.Text("", size=(12, 1)), sg.Button("Submit", key='feedback_ok', size=(25, 1),
        tooltip="Click here to send your feedback."), sg.Text("", size=(7, 1)),
     sg.Button("Cancel", key='feedback_can', size=(25, 1), tooltip="Click here to go back.")],
    [sg.HSeparator()],
]

# Main app layout
main_layout = [
    [sg.Menu(menu_def, tearoff=False, key="menu")],
    [sg.Column(user_name_pen, key="username", visible=True, justification='center')],
    [sg.Column(home_layout, key='home', visible=True, ),
     sg.Column(layout_pension, key="pen_display", visible=False, ),
     sg.Column(gra_layout, key="gra_display", visible=False, ),
     sg.Column(leave_calculator_layout, key="leave_cal", visible=False, ),
     sg.Column(feedback_layout, key="feedback_layout", visible=False, )],
]

new_menu_def = menu_def

window = sg.Window("Basic Retirement Benefits Calculator for employees of WB Govt. (Offline Application)", main_layout,
                   size=(755, 600), resizable=False, icon=r'icon.ico', finalize=True, enable_close_attempted_event=True)
