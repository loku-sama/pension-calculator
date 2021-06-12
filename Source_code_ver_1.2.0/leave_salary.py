"""
##############################################   READ ME   ############################################
Leave Salary Calulator Function File
Author - Sourav(Loku)

#######################################################################################################
"""
import layout


def leave_salary_calculation_main(basic_pay, da, ma, leave_due, wbhs):
    try:
        total_pay = basic_pay + da + ma

        def check_basic_pay(n):
            """ Function for checking minimum basic pay as per ROPA 2019. """
            if n < 17000:
                layout.sg.Popup("Basic Pay can not be less than Rs.17000 as per ROPA 2019", title="Error!",
                                icon=r'icon.ico')
            elif n >= 17000:
                n = basic_pay
            return n

        check_basic_pay(basic_pay)
        if wbhs:
            ma = 500
            layout.window["ma"].update(ma)
            layout.window.refresh()
        else:
            ma = 0
            layout.window["ma"].update(ma)
            layout.window.refresh()

        layout.window['total-pay'].update(total_pay)

        def calculate_leave_salary(tp, leave):
            """ Function for calculating leave salary amount. """
            leave_salary = 0
            if leave_due > 300:
                layout.sg.Popup("Maximum leave due can not exceed 300 days.", title="Error!",
                                icon=r'icon.ico')
                layout.window['leave-sal'].update("Error! Leave due exceeds 300 days. Try again.")
            elif leave_due <= 300 and basic_pay >= 17000:
                leave_salary = round((tp * leave) / 30)
                layout.window['leave-sal'].update(leave_salary)
            else:
                leave_salary = 0
                layout.window['leave-sal'].update(leave_salary)
            return leave_salary

        calculate_leave_salary(total_pay, leave_due)
        layout.window['leave_report'].update(disabled=False)
    except:
        pass


def leave_salary_report(template_var_leave):
    """ Function to generate report """
    html_out = layout.template_leave.render(template_var_leave)
    file_name = f"leave_salary_report_{layout.time_stamp}.html"  # Makes a dynamic filename everytime
    with open(f"./reports/{file_name}", "w") as f:
        f.write(html_out)
    f.close()
    layout.sg.webbrowser.open(url=f"{layout.current_directory}/reports/{file_name}", new=2)
