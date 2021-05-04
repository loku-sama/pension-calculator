import layout
import pension
import gratuity
import leave_salary
from datetime import datetime

while True:
    event, values = layout.window.read()
    if event == "Exit" or event == layout.sg.WIN_CLOSED:
        break  # Breaks the main loop if the user closes the layout.window

    if event == 'Home':
        layout.window['pen_display'].update(visible=False)
        layout.window['gra_display'].update(visible=False)
        layout.window['leave_cal'].update(visible=False)
        layout.window['home'].update(visible=True)
    if event == "pen" or event == "Pension Calculator":
        layout.window['pen_display'].update(visible=True)
        layout.window['gra_display'].update(visible=False)
        layout.window['leave_cal'].update(visible=False)
        layout.window['home'].update(visible=False)
    if event == "gra" or event == "Gratuity Calculator":
        layout.window['gra_display'].update(visible=True)
        layout.window['pen_display'].update(visible=False)
        layout.window['leave_cal'].update(visible=False)
        layout.window['home'].update(visible=False)
    if event == "leave" or event == "Leave Salary Calculator":
        layout.window['leave_cal'].update(visible=True)
        layout.window['gra_display'].update(visible=False)
        layout.window['pen_display'].update(visible=False)
        layout.window['home'].update(visible=False)
    if event == "git":
        layout.sg.webbrowser.open(url='https://github.com/loku-sama/pension-calculator', new=2)
    if event == "fsm":
        layout.sg.Popup("The free software movement is a social movement with the goal of obtaining and guaranteeing "
                        "certain "
                        "freedoms for software users, namely the freedom to run the software, to study the software, "
                        "to modify the software, to share possibly modified copies of the software. Software which "
                        "meets these requirements is termed free software. The word 'free' is ambiguous in English, "
                        "although in this context, it means 'free as in freedom', not 'free as in zero price'."
                        "\nSource: Wikipedia", title="Free "
                                                     "Software Movement", custom_text="Close",
                        icon=r'icon.ico', )
    if event == 'Know More':
        layout.sg.webbrowser.open(url='https://en.wikipedia.org/wiki/Free_software_movement', new=2)

    if event == "Submit":
        name = values['name']
        if name != "User_Name" or not " ":
            layout.window["display_name"].update(name)
        else:
            layout.sg.Popup("Please Enter Your Name.")

    if event == "About":
        layout.sg.popup("Basic Retirement Benefits Calculator for employees of Govt. of West Bengal.\nVersion - 1.1.0\n"
                        "App coded by SOURAV, Language- Python and a little HTML."
                        "\nApp programmed on the basis of latest Govt. rules and Orders."
                        "\nThis is for informational purpose only. Please refer original Rules and Orders thoroughly.\n"
                        "This application is Open Source and licensed under GNU Public License V.3. You can download "
                        "the "
                        "source code from Github. \nThis app will get updated in case of any change in rules and "
                        "orders. "
                        " Always download the latest release from the Github page.",
                        title="About",
                        icon=r'icon.ico', )
    if event == 'Fork Me on Github':
        layout.sg.webbrowser.open(url='https://github.com/loku-sama', new=2, )
    if event == 'Check for Updates':
        layout.sg.webbrowser.open(url='https://github.com/loku-sama/pension-calculator/releases/', new=2, )
    if event == 'Rules and Orders':
        layout.sg.webbrowser.open(url='http://www.wbfin.nic.in/New_Fin/Pages/Publication.aspx', new=2, )
    if event == 'gnu':
        layout.sg.webbrowser.open(url='https://www.gnu.org/gnu/linux-and-gnu.html', new=2, )
    if event == 'python':
        layout.sg.webbrowser.open(url='https://www.python.org/', new=2, )

    if event == "CALCULATE":
        pension.pension_calculation_main(datetime.strptime(values["dojPick"], layout.format_date),
                                         datetime.strptime(values["dorPick"], layout.format_date),
                                         int(values['basic']), int(values['npa1']), int(values['comm']),
                                         int(values['factor']))

    if event == "pen_report":
        try:
            template_var_pension = {"user_name": values['name'], "bp": values['Bpen'], "rp": values['Rpen'],
                                    "fp": values['Fpen'], "doj": values['dojPick'], "dor": values['dorPick'],
                                    "lp": values['total-pay-pen'], "comm": values['comm'], "qs": values['xx'],
                                    "sp": values['q_service'], "cvp": values['cvp'], "age": values['factor']}
            pension.pension_report(template_var_pension)
        except:
            layout.sg.Popup("Something went horribly wrong. Please try againg or report the bug.", title="Error!",
                            icon=r'icon.ico')

    if event == "cal_gra":
        gratuity.gratuity_calculation_main(datetime.strptime(values["dojPick1"], layout.format_date),
                                           datetime.strptime(values["dorPick1"], layout.format_date),
                                           int(values['basic1']), int(values['da']), int(values['npa']),
                                           )
    if event == "gra_report":
        try:
            template_var_gratuity = {"user_name": values['name'], "rg": values['Rgra'], "dg": values['Dgra'],
                                     "doj": values['dojPick1'], "dor": values['dorPick1'],
                                     "lp": values['total-pay-gra'],
                                     "qs": values['xx1'], "sp": values['q_service1']}
            gratuity.gratuity_report(template_var_gratuity)
        except:
            layout.sg.Popup("Something went horribly wrong. Please try againg or report the bug.", title="Error!",
                            icon=r'icon.ico')

    if event == "wbhs-no":
        ma = 500
        layout.window["ma"].update(ma)
    else:
        ma = 0
        layout.window["ma"].update(ma)

    if event == "cal_leave":
        leave_salary.leave_salary_calculation_main(int(values['basic2']), int(values['da1']), int(values['ma']),
                                                   int(values['leave-due']), values['wbhs-no'])

    if event == "leave_report":
        try:
            template_var_leave = {"user_name": values['name'], "lp": values['total-pay'], "leave": values['leave-due'],
                                  "leave_sal": values['leave-sal']}
            leave_salary.leave_salary_report(template_var_leave)
        except:
            layout.sg.Popup("Something went horribly wrong. Please try againg or report the bug.", title="Error!",
                            icon=r'icon.ico')


layout.window.close()
