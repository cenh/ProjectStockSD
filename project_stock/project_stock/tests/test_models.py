from django.test import TestCase
from project_stock.models import Group, Project, Publication, Supervisor
from django.core.exceptions import ValidationError

class TestSupervisor(TestCase):
    def test_create_no_attributes(self):
        """Try and create a supervisor without setting any attributes

        This should fail with ValidationError
        """
        sup = Supervisor()
        with self.assertRaises(ValidationError):
            sup.full_clean()

    def test_create_necessary_attributes(self):
        """Try and create a supervisor with the necessary attributes

        This should pass
        """
        sup = Supervisor()
        sup.first_name = 'Arthur'
        sup.last_name = 'Anderson'
        sup.email = 'arthur.anderson@andersons.com'
        sup.full_clean()

    def test_invalid_websites(self):
        """Try and submit supervisor with an invalid website URL

        This should fail
        """
        invalid_urls = ['invalidwebsite',
                        'htt://example.com',
                        'example.com']
        sup = Supervisor()
        sup.first_name = 'Arthur'
        sup.last_name = 'Anderson'
        sup.email = 'arthur.anderson@andersons.com'
        for u in invalid_urls:
            sup.website = u
            with self.assertRaises(ValidationError):
                sup.full_clean()

    def test_valid_websites(self):
        """Try and submit supervisors with various valid website URLs

        This should pass
        """
        valid_urls = ['http://example.com',
                      'https://docs.python.org/3/library/unittest.html#basic-example',
                      'https://example.com?user=arthur&password=arthurspassword']
        sup = Supervisor()
        sup.first_name = 'Arthur'
        sup.last_name = 'Anderson'
        sup.email = 'arthur.anderson@andersons.com'
        for u in valid_urls:
            sup.website = u
            sup.full_clean()
