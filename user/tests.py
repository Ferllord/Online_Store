from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import User, EmailVerification

class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:register')
        self.data = {
            'first_name': 'Valery',
            'last_name': 'Ivanov',
            'username': 'valery',
            'email': 'valery@gmail.com',
            'password1': '12345678aP',
            'password2': '12345678aP'
        }


    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'user/register.html')

    def test_user_registration_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # self.assertRedirects(response,reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verif = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verif.exists())