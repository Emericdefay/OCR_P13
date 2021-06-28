# Django Libs:
from django.test import TestCase
from django.urls import reverse
# Local Libs:
from lettings.models import Letting, Address


class TestsLettings(TestCase):
    """Test lettings apps"""

    def setUp(self) -> None:
        """Initialize models
        """
        # Address test
        address = Address(**{
            'id': 1,
            'number': 1,
            'street': 'street_test',
            'city': 'city_test',
            'state': 'state_test',
            'zip_code': 11111,
            'country_iso_code': 'USA',
        })
        address.save()

        # Letting test
        letting = Letting(**{
            'id': 1,
            'title': 'test_letting',
            'address_id': 1
        })
        letting.save()

    def test_lettings_index(self):
        """letting index page should contain
        <title>Lettings</title>
        """
        response = self.client.get(reverse('lettings:index'))
        attempted_contain = b'<title>Lettings</title>'
        self.assertEqual(True, attempted_contain in response.content)

    def test_lettings_letting(self):
        """Getting a letting, page should contains:
        <title>{{ title }}</title>
        So let check if title contains the letting title.
        """
        letting_id = '1'
        response = self.client.get(
            reverse('lettings:letting',
                    kwargs={'letting_id': letting_id})
                )
        title = 'test_letting'
        attempted_contain = bytes(
            f"<title>{title}</title>", 'utf-8')
        self.assertEqual(True, attempted_contain in response.content)
