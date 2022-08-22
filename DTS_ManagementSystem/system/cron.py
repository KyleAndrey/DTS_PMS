from django.conf import settings
from django.core.mail import send_mail

def emailDeadline():
    nearDeadlines = Project.objects.filter(projectStatus='Ongoing',projectDeadline__range=[now(),now() + datetime.timedelta(days = 3)])
    for proj in nearDeadlines:
        subject = 'Deadline is near'
        message = f'The project ' + proj.projectName + ' will be due on ' + proj.projectDeadline + '. Please take appropriate actions, Thank you'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail( subject, message, email_from, recipient_list )
        print('email')