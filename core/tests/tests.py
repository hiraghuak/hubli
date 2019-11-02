from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your tests here. 
class ModelTests(TestCase):
    
    def test_creating_user_with_email_successfull(self):
        """ test creating a new user with an email is successfully"""

        email = 'test@gmail.com'
        password = 'test@321'
        user = get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test@321')

        self.assertEqual(user.email, email.lower())
        