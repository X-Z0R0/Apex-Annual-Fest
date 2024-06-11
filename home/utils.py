# from participantINFO.models import Student
import time
from django.core.mail import send_mail
from django.conf import settings

def run_this_funtion():
    print("function started")
    print("function started...")

    time.sleep(2)
    print("fucntion executed")

def send_email_to_client(TeamID,Game,email):
    subject = "Apex Annual Fest Registration Successfull"
    message = f'Congratulations, your payment is successfull.\nYou register in game={Game}, and your team id is={TeamID}.\n Thank you for successfully registering for Apex University Annual Fest Program! Your participation is greatly appreciated.\nBest Regards,\nStudent Council'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [str(email)]
    send_mail(subject,message,from_email,recipient_list)
