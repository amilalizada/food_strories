from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import  EmailMultiAlternatives
from django.template import RequestContext
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Subscriber
from stories.models import Recipe
from celery import shared_task


@shared_task
def send_mail_custom():
    subs = Subscriber.objects.values_list('email')
    recipes = Recipe.objects.all()
    subject = 'Our famuos recipes'
    message = render_to_string('email-subscribers.html', {
        # 'user': user,
        'recipes': recipes,
        # 'domain': current_site,
        # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # 'token': account_activation_token.make_token(user),
    })
    msg = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=subs)
    msg.attach_alternative(message, "text/html")
    msg.send()