from django.test import TestCase
from django.core.cache import cache
from django.core.urlresolvers import reverse


class CoreViewsTestCase(TestCase):
    def setUp(self):
        """ Reset cache at the beginning of each test """
        cache.clear()

    def test_home_view(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

        # Cached view doesn't render template again
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'pages/home.html')
