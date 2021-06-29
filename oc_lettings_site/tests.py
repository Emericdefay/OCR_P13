# Django Libs:
from django.test import TestCase
from django.urls import reverse


class TestsHomepage(TestCase):
    """Test homme app"""
    def test_home_index(self):
        """home index page should contain
        <title>Holiday Homes</title>
        """
        response = self.client.get(reverse('index'))
        attempted_contain = b'<title>Holiday Homes</title>'
        self.assertEqual(True, attempted_contain in response.content)
