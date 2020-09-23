from django.urls import reverse, resolve


class TestUrls:

    def test_signup_url(self):
        path = reverse('account_signup')
        assert resolve(path).view_name == 'account_signup'
