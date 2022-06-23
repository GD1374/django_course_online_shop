from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


class SignUpFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='user1')

    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
