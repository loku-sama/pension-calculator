"""
##############################################   READ ME   ############################################
Gratuity Calulator Function File
Author - Sourav(Loku)

#######################################################################################################
"""

from dateutil import relativedelta
import layout


def gratuity_calculation_main(doa, dor, basic_pay, da, oth):
    try:
        diff = relativedelta.relativedelta(dor, doa)
        year = diff.years
        mon = diff.months
        days = diff.days
        six_monthly_installment = year * 2
        total_pay = basic_pay + da + oth

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

        qua_service_in_months_gra = qualifying_ins_calculation(mon, six_monthly_installment)

        def check_basic_pay(n):
            """ Function for checking minimum basic pay as per ROPA 2019. """
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
            """ Function for calculating the retiring Gratuity amount. """
            if y < 10 and basic_pay >= 17000:
                retiring_gratuity = round((tp * qua_service_in_months_gra) / 2)
            elif y >= 10 and basic_pay >= 17000:
                retiring_gratuity = round((tp * qua_service_in_months_gra) / 4)
            else:
                retiring_gratuity = 0
            return round(retiring_gratuity)

        retiring_gratuity = get_retiring_gratuity(year, total_pay)

        def get_death_gratuity(y, tp):
            """ Function for calculating the death Gratuity amount. """
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
            """ Function for checking maximum limit of Gratuity amount as per ROPA 2019. """
            if gra > 1200000:
                gra = 1200000
            return gra

        layout.window['Rgra'].update(check_gratuity(retiring_gratuity))
        layout.window['Dgra'].update(check_gratuity(death_gratuity))
        layout.window['gra_report'].update(disabled=False)

    except:
        pass


def gratuity_report(template_var_gratuity):
    html_out = layout.template_gra.render(template_var_gratuity)
    with open(f"gratuity report.html", "w") as f:
        f.write(html_out)
    f.close()
    layout.sg.webbrowser.open(url="gratuity report.html", new=2)
