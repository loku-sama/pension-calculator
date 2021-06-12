"""
##############################################   READ ME   ############################################
Pension Calulator Function File
Author - Sourav(Loku)

#######################################################################################################
"""

from dateutil import relativedelta
import layout


def pension_calculation_main(doa, dor, basic_pay, npa, com, age):
    try:
        diff = relativedelta.relativedelta(dor, doa)
        year = diff.years
        mon = diff.months
        days = diff.days  # Optional
        six_monthly_installament = year * 2
        total_pay = basic_pay + npa

        def qualifying_ins_calculation(mon, six_ins):
            """ Function for calculating the net qualifying service period in 6 monthly installments. """
            if (mon >= 3) and (mon < 6):
                qua_service_in_months = six_ins + 1
            elif (mon >= 6) and (mon < 9):
                qua_service_in_months = six_ins + 1
            elif (mon >= 9) and (mon < 12):
                qua_service_in_months = six_ins + 2
            else:
                qua_service_in_months = six_ins
            return qua_service_in_months

        qua_service_in_months = qualifying_ins_calculation(mon, six_monthly_installament)

        def check_basic_pay(n):
            """ Function for checking the minimum basic pay as per ROPA 2019. """
            if n < 17000:
                layout.sg.Popup("Basic Pay can not be less than Rs.17000 as per ROPA 2019", title="Error!",
                                icon=r'icon.ico')
            elif n >= 17000:
                n = basic_pay
            return n

        check_basic_pay(basic_pay)
        layout.window['total-pay-pen'].update(total_pay)
        layout.window['q_service'].update("{} years {} months".format(year, mon))

        if year < 10:
            layout.window['xx'].update(qua_service_in_months)
            family_pension = round((total_pay * 30) / 100)
            layout.sg.Popup("Sorry! You are not eligible for Regular Pension.", title="Error!",
                            icon=r'icon.ico')
            layout.window['Fpen'].update(family_pension)
            # return family_pension
        elif year > 20:
            qua_service_in_months = 40
            layout.window['xx'].update(qua_service_in_months)
        else:
            layout.window['xx'].update(qua_service_in_months)

        def check_commutation(com):
            """ Function for checking the pension commutation limits as per ROPA 2019. """
            if com > 40:
                layout.sg.Popup("Commutation must not exceed 40%. Try again.", title="Error!",
                                icon=r'icon.ico')
                commutation = 100
                layout.window['pen_report'].update(disabled=True)
            else:
                commutation = com
            return commutation

        commutation = check_commutation(com)

        def get_pension(a, b, qsm):
            """ Function for calculating basic pension. """
            bp = 0
            if 20 < qsm < 40 and b <= 40:
                bp = ((a / 2) * qsm) / 40
            elif qsm >= 40 and b <= 40:
                bp = a / 2
            elif qsm > 20 and b > 40:
                bp = ((a / 2) * qsm) / 40
            elif qsm >= 40 and b > 40:
                bp = a / 2
            return bp

        basic_pension = get_pension(total_pay, commutation, qua_service_in_months)

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

        layout.window['Bpen'].update(round(determine_basic_pension(basic_pension)))
        final_basic_pension = determine_basic_pension(basic_pension)

        def determine_reduced_pension(pen, comm):
            """ Function for calculating reduced basic pension. """
            pension = 0
            if comm == 0:
                pension = round(pen)
            elif 1 <= comm <= 40:
                pension = round(pen - (pen * comm / 100))
            elif comm > 40:
                pension = "Error! Commutation must not exceed 40%."
            return pension

        layout.window['Rpen'].update(determine_reduced_pension(final_basic_pension, commutation))

        def get_family_pension(pay):
            """ Function for calculating Family pension. """
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

        layout.window['Fpen'].update(get_family_pension(total_pay))

        def get_cvp():
            """ Function for calculating Commuted value of pension. """
            if age < 20 or age > 81:
                layout.sg.Popup("Age as on next Birthday must be between 20 to 81.", title="Error", icon=r'icon.ico')
                cvp = 0
                return cvp
            if basic_pay < 17000:
                cvp = 0
                return cvp
            factor = {20: 9.188, 41: 9.075, 62: 8.093, 21: 9.187, 42: 9.059, 63: 7.982, 22: 9.186, 43: 9.040,
                      64: 7.862, 23: 9.185, 44: 9.019, 65: 7.731, 24: 9.184, 45: 8.996, 66: 7.591, 25: 9.183,
                      46: 8.971, 67: 7.431, 26: 9.182, 47: 8.943, 68: 7.262, 27: 9.180, 48: 8.913, 69: 7.083,
                      28: 9.178, 49: 8.881, 70: 6.897, 29: 9.176, 50: 8.846, 71: 6.703, 30: 9.173, 51: 8.808,
                      72: 6.502, 31: 9.169, 52: 8.768, 73: 6.296, 32: 9.164, 53: 8.724, 74: 6.085, 33: 9.159,
                      54: 8.678, 75: 5.872, 34: 9.152, 55: 8.627, 76: 5.657, 35: 9.145, 56: 8.572, 77: 5.443,
                      36: 9.136, 57: 8.512, 78: 5.229, 37: 9.126, 58: 8.446, 79: 5.018, 38: 9.116, 59: 8.371,
                      80: 4.812, 39: 9.103, 60: 8.287, 81: 4.611, 40: 9.090, 61: 8.194}  # Cumulative factors
            com_pen_per_month = (basic_pension * commutation) / 100
            f = factor.get(age, 0)
            cvp = round(com_pen_per_month * 12 * f)
            return cvp

        comm_value = get_cvp()
        layout.window['cvp'].update(comm_value)
        layout.window['pen_report'].update(disabled=False)
    except:
        pass


def pension_report(template_var_pension):
    """ Function to generate report """
    html_out = layout.template_pen.render(template_var_pension)
    file_name = f"pension_report_{layout.time_stamp}.html"  # Makes a dynamic filename everytime
    with open(f"./reports/{file_name}", "w") as f:
        f.write(html_out)
    f.close()
    layout.sg.webbrowser.open(url=f"{layout.current_directory}/reports/{file_name}", new=2)
