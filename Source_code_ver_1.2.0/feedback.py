"""
##############################################   READ ME   ############################################
Feedback submission Function File
Author - Sourav(Loku)
#######################################################################################################
"""

import smtplib  # For creating SMTP Server
import ssl  # For creating SSL connection
from email.mime.text import MIMEText  # For making emails
import urllib.request  # Foe checking internet connection


class Feedback:
    def __init__(self, login_id, password):
        """ Feedback class constructor """
        self.login_id = login_id  # Log in ID of the mail account from which you want to send the Feedback
        self.password = password  # Password of the mail account from which you want to send the Feedback
        self.context = ssl.create_default_context()  # Creates SSL connection

    def send_feedback(self, user_name, user_email, user_feedback):
        """" Function for sending the feedback """
        try:
            server = smtplib.SMTP("smtp.office365.com", 587)  # SMTP Server IP and Port of your provider
            server.ehlo()  # Optional
            server.starttls(context=self.context)  # Starts TLS handshake
            server.login(self.login_id, self.password)  # Signing to your account
            email_body = f"Name : {user_name}\nemail : {user_email}\nFeedback : {user_feedback}"
            SUBJECT = 'Feedback of Retirement Benefit Calculator ver 1.2.0'
            TO = 'happysourav96@gmail.com'
            FROM = self.login_id  # Mail id from where feedback will be sent
            msg = MIMEText(email_body)  # Mail body
            msg['Subject'] = SUBJECT  # Mail Subject
            msg['To'] = TO  # Mail to
            msg['From'] = FROM  # Mail form
            server.sendmail(FROM, TO, msg.as_string())  # Sending the mail
            return True
        except:
            return False
        finally:
            server.quit()  # Quits the server


def connect(host='http://google.com'):
    """ Function for checking the Internet Connection """
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def check_mail(email):
    """ Function for checking valid email user input """
    if "@" in str(email) and "." in str(email):
        return True
    else:
        return False
