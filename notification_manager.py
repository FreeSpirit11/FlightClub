import os
from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
import smtplib
my_email="my697253@gmail.com"
password="xxfrwtezcpgvqgls"
my_twilio_num = '+12542805765'

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message,user_num):
        message = self.client.messages \
            .create(
            body=message,
            from_=my_twilio_num ,
            to = user_num
        )
        

    def send_emails(self, message, user_email):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=user_email,
                                msg=message,
                                )


