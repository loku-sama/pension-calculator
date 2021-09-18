"""
##############################################   READ ME   ############################################
Gratuity Calculator Function File
Author - Sourav(Loku)

#######################################################################################################
"""

from dateutil import relativedelta
import layout


def gratuity_calculation_main(doa, dor, basic_pay, da, oth):
    """ Main Pension Calculator function

    :param doa: Date of joining as string
    :type doa: date
    :param dor: Date of Retirement or Death as string
    :type dor: date
    :param basic_pay: Last Basic Pay (Must be greater than 17000)
    :type basic_pay: int
    :param da: Da (if any)
    :type da: int
    :param oth: Other Allowance (if any)
    :type oth: int
    """
    try:
        diff = relativedelta.relativedelta(dor, doa)
        year = diff.years
        mon = diff.months
        days = diff.days  # Optional
        six_monthly_installment = year * 2
        total_pay = basic_pay + da + oth

        def qualifying_ins_calculation(mon, six_ins):
            """ Function for calculating the net qualifying service period in 6 monthly installments.

            :param mon: Total No. of months
            :type mon: int
            :param six_ins: Six monthly instalments (mon * 2)
            :type six_ins: int
            :return: Qualifying Service period as per Govt. rules
            :rtype: int
            """
            if (mon >= 3) and (mon < 6):
                qua_service_in_months = six_ins + 1
            elif (mon >= 6) and (mon < 9):
                qua_service_in_months = six_ins + 1
            elif (mon >= 9) and (mon < 12):
                qua_service_in_months = six_ins + 2
            else:
                qua_service_in_months = six_ins
            return qua_service_in_months

        qua_service_in_months_gra = qualifying_ins_calculation(mon, six_monthly_installment)

        def check_basic_pay(n):
            """ Function for checking the minimum basic pay as per ROPA 2019.

            :param n: Basic Pay entered by User
            :type n: int
            :return: Basic Pay is it is greater than 17000 else shows an error message.
            :rtype: int
            """
            if n < 17000:
                layout.sg.Popup("Basic Pay can not be less than Rs.17000 as per ROPA 2019", title="Error!",
                                icon=r'icon.ico')
            elif n >= 17000:
                n = basic_pay
            return n

        check_basic_pay(basic_pay)
        layout.window['total-pay-gra'].update(total_pay)
        layout.window['q_service1'].update("{} years {} months".format(year, mon))
        if year >= 33:
            qua_service_in_months_gra = 66
            layout.window['xx1'].update(qua_service_in_months_gra)
        else:
            layout.window['xx1'].update(qua_service_in_months_gra)

        def get_retiring_gratuity(y, tp):
            """  Function for calculating the retiring Gratuity amount.

            :param y: Qualifying service in years
            :type y: int
            :param tp: Total pay
            :type tp: int
            :return: Retiring Gratuity calculated as per Govt. rules.
            :rtype: int
            """
            if y < 10 and basic_pay >= 17000:
                retiring_gratuity = round((tp * qua_service_in_months_gra) / 2)
            elif y >= 10 and basic_pay >= 17000:
                retiring_gratuity = round((tp * qua_service_in_months_gra) / 4)
            else:
                retiring_gratuity = 0
            return round(retiring_gratuity)

        retiring_gratuity = get_retiring_gratuity(year, total_pay)

        def get_death_gratuity(y, tp):
            """  Function for calculating the Death Gratuity amount.

            :param y: Qualifying service in years
            :type y: int
            :param tp: Total pay
            :type tp: int
            :return: Death Gratuity calculated as per Govt. rules.
            :rtype: int
            """
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

        death_gratuity = get_death_gratuity(year, total_pay)

        def check_gratuity(gra):
            """  Function for checking maximum limit of Gratuity amount as per ROPA 2019.

            :param gra: Retiring or Death Gratuity calculated above.
            :type gra: int
            :return: If gratuity exceeds 1200000, it limits it on 1200000 as per Govt. rule.
            :rtype: int
            """
            if gra > 1200000:
                gra = 1200000
            return gra

        layout.window['Rgra'].update(check_gratuity(retiring_gratuity))
        layout.window['Dgra'].update(check_gratuity(death_gratuity))
        layout.window['gra_report'].update(disabled=False)

    except:
        pass


def gratuity_report(template_var_gratuity):
    """  Function to generate report

    :param template_var_gratuity: List of Values as Dictionary to be rendered in the HTML template file.
    :type template_var_gratuity: dict
    """
    html_out = layout.template_gra.render(template_var_gratuity)
    file_name = f"gratuity_report_{layout.time_stamp}.html"  # Makes a dynamic filename everytime
    with open(f"./reports/{file_name}", "w") as f:
        f.write(html_out)
    f.close()
    layout.sg.webbrowser.open(url=f"{layout.current_directory}/reports/{file_name}", new=2)
