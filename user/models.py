from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images',null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)



class EmailVerification(models.Model):
    code  = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'Email verification object fro {self.user.email}'


    def send_verification_email(self):
        host = "http://127.0.0.1:8000"
        url = host + reverse('users:email_verification',kwargs={'email': self.user.email,'code' : self.code })
        subject = f'Подтверждение учетной записи для {self.user.username}'
        text = f'Для подтверждение учетной записи перейдите по {url}'
        mail = settings.EMAIL_HOST_USER
        send_mail(
            f'{subject}',
            f'{text}',
            f'{mail}',
            [f'{self.user.email}'],
        )

    def is_expired(self):
        return now() >= self.expiration
