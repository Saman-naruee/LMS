from rest_framework import status
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.infras.tests.base_tests import BaseViewTestClass
from custom_logger import custom_logger as print


class FetchUserInfos(BaseViewTestClass):
    def setUp(self):
        super().setUp()
        self.client = APIClient()

    def test_fetch_users_data(self):
        response = self.client.get(self.users_url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
