from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, FriendRequest
# Create your tests here.
from django.db import transaction




class ProfileTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        # Create a user for this test
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK'
        )
        test_user1.save()

        # Create profile for this test
        test_profile = Profile.objects.create(
            user=test_user1,
            bio = 'This is a test bio',
        )
        test_profile.save()
    
    def test_profile_content(self):
        profile = Profile.objects.get(id=1)
        expected_object_name = f'{profile.user}'
        bio = f'{profile.bio}'
        self.assertEquals(expected_object_name, 'testuser1')
        self.assertEquals(bio, 'This is a test bio')
        