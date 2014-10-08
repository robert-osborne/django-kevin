from django.test import TestCase
from django.core.urlresolvers import reverse

from accounts.factories import TestUserFactory


class AuthtoolsViewsExtensionsTestCase(TestCase):
    def setUp(self):
        """ Create a user and log in """
        self.user = TestUserFactory(email='test@example.com')
        self.client.login(email='test@example.com', password='123')

    def test_logout_view_extension(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logout.html')

    def test_password_reset_view_extension(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset.html')

    def test_password_change_view_extension(self):
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_change.html')

        password_change_payload = {'old_password': '123', 'new_password1': 'lol', 'new_password2': 'lol'}
        response = self.client.post(reverse('password_change'), password_change_payload)
        self.assertRedirects(response, reverse('password_change_done'))

        # Test to make sure session is still logged in after password change
        self.assertIn('_auth_user_id', self.client.session)
