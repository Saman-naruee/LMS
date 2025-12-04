from django.test import TestCase
from apps.courses.models import Course
from apps.accounts.models import User # Import the User model
from django.urls import reverse
from datetime import datetime
from django.utils import timezone


class CourseCreateTest(TestCase):
    def setUp(self):
        self.url = reverse('create-course')
        # Provide a phone_number when creating the user
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='password',
            phone_number=1234567890
        )
        print(self.user.id)
    def test_create_course_returns_201(self):
        start_date = timezone.make_aware(datetime(2025, 1, 1, 9, 0, 0))
        end_date = timezone.make_aware(datetime(2025, 1, 31, 17, 0, 0))

        payload = {
            "title": "Test Course",
            "teacher": self.user.id,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
        }
        response = self.client.post(self.url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Course.objects.filter(title="Test Course").exists())
