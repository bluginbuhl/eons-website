from django.test import TestCase
from django.contrib.auth import get_user_model
from guardian.shortcuts import assign_perm

from eons_data.models import EonsSite


User = get_user_model()

class EonsSiteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        TEST_SITE_CODE = 'E005'
        TEST_SITE_NAME = 'Eons Test Site 5'
        TEST_SITE_LAT = 35.198284
        TEST_SITE_LONG = -111.651299

        TEST_USER_EMAIL = 'admin1@eons.com'
        TEST_USER_PASS = 'testpass123'

        test_user = User.objects.create(
            email = TEST_USER_EMAIL,
            password = TEST_USER_PASS
        )

        test_site = EonsSite.objects.create(
            site_code = TEST_SITE_CODE,
            name = TEST_SITE_NAME,
            latitude = TEST_SITE_LAT,
            longitude = TEST_SITE_LONG
        )


    def setUp(self):
        self.site = EonsSite.objects.get(site_code='E005')
        self.user = User.objects.get(email='admin1@eons.com')
        assign_perm("upload_data", self.user, self.site)

    def test_site_fields(self):
        self.assertNotEqual(self.site.site_code, 'E001')
        self.assertEqual(self.site.name, 'Eons Test Site 5')
        self.assertEqual(self.site.latitude, 35.198284)
        self.assertEqual(self.site.longitude, -111.651299)

    def test_site_users_list(self):
        self.assertEqual(self.site.users_list()[0].email, 'admin1@eons.com')

    def test_site_string_representation(self):
        new_site = EonsSite.objects.create(
            site_code = 'E008'
        )
        self.assertEqual(new_site.__str__(), 'E008')
        new_site.name = 'Site Name'
        self.assertEqual(new_site.__str__(), 'E008 - Site Name')


