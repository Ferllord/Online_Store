from celery import shared_task
from .models import User, EmailVerification
from django.utils.timezone import now
from datetime import timedelta
import uuid


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    code = uuid.uuid4()
    record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
    record.send_verification_email()
