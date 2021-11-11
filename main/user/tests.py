from django.test import TestCase
from .models import User
from django.contrib.auth import authenticate

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="harshit675@gmail.com",
            password="harshith",
            first_name="Harshith",
            last_name="sheggam",
        )
        self.email = "harshit675@gmail.com"
        self.password = "harshith"

    def tearDown(self):
        self.user.delete()

    def test_user_exists(self):
        """User created test"""
        email = "harshit675@gmail.com"
        user = User.objects.get(email=email)
        self.assertEqual(
            user.email, "harshit675@gmail.com", f"This value should be {email}"
        )
        print("User verifed test ------------------- ok ")

    def test_wrong_username(self):
        user = authenticate(username="wrong", password="12test12")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(email=self.email, password="wrong")
        self.assertFalse(user is not None and user.is_authenticated)
