from CalendarAPI.celery import app
from celery import shared_task
from .models import Events
import datetime
from CalendarAPI.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@app.task
def mail_sender(id):
    event=Events.objects.get(id=id)
    email=event.user.email
    subject=event.summary
    plain_message="Событие начнётся в "+str(event.time_from)
    print("Goes")
    try:
        send_mail(subject, plain_message, EMAIL_HOST_USER, [email])
    except Exception as e:
        print(e)
