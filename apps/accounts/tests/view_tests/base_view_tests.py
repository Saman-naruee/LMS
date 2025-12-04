from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from apps.accounts.models import User


class BaseViewTestClass(APITestCase):
    def setUp(self):
        self.users_url = reverse('users-list')
        self.users = User.objects.all()
