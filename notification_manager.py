from twilio.rest import Client
import smtplib

ACCOUNT_SID = "AC6d066e58affc4e3fc06332a66c630e25"
AUTH_TOKEN = "d3934e03fbef686a19dc3250980e5618"
SENDER_NUMBER = "+15628421413"
RECEIVER_NUMBER = "+995593601624"
SENDER_EMAIL = "sina_eshrati@yahoo.com"
SENDER_EMAIL_PASSWORD = "euolagjhjfqaiddm"


class NotificationManager:

    def send_message(self, message):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
                body=message,
                from_=SENDER_NUMBER,
                to=RECEIVER_NUMBER
            )

    def send_email(self, message, receiver_email):
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
            connection.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
            connection.sendmail(SENDER_EMAIL, receiver_email,
                                msg=f"Subject:Sina's flight club\n\n{message}".encode("utf-8"))
