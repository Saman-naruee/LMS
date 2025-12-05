from rest_framework import status
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.accounts.tests.view_tests.base_view_tests import BaseViewTestClass

class FetchUserInfos(BaseViewTestClass):
    def setUp(self):
        super().setUp()  # Call the parent class's setUp method
        self.client = APIClient()

    def test_fetch_users_data(self):
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
