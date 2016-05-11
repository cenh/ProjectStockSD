from django.test import TestCase
from project_stock.models import Group, Project, Publication, Supervisor
from django.core.exceptions import ValidationError

class TestSupervisor(TestCase):
    def createNoAttributes(self):
        """Try and create a supervisor without setting any attributes

        This should fail with ValidationError
        """
        sup = Supervisor()
        with self.assertRaises(ValidationError):
            sup.full_clean()

    def createNecessaryAttributes(self):
        """Try and create a supervisor with the necessary attributes

        This should pass
        """
        sup = Supervisor()
        sup.first_name = "Arthur"
        sup.last_name = "Anderson"
        sup.email = "arthur.anderson@andersons.com"
        sup.full_clean()

    def invalidWebsite(self):
        """Try and submit supervisor with an invalid website URL

        This should fail
        """
        sup = Supervisor()
        sup.first_name = "Arthur"
        sup.last_name = "Anderson"
        sup.email = "arthur.anderson@andersons.com"
        sup.website = "invalidwebsite"
        with self.assertRaises(ValidationError):
            sup.full_clean()

    def validWebsite(self):
        """Try and submit supervisor with an valid website URL

        This should pass
        """
        sup = Supervisor()
        sup.first_name = "Arthur"
        sup.last_name = "Anderson"
        sup.email = "arthur.anderson@andersons.com"
        sup.website = "example.com"
        sup.full_clean()

    def validWebsiteComplex(self):
        """Try and submit supervisor with a complex but valid website URL

        This should pass
        """
        sup = Supervisor()
        sup.first_name = "Arthur"
        sup.last_name = "Anderson"
        sup.email = "arthur.anderson@andersons.com"
        sup.website = "https://docs.python.org/3/library/unittest.html#basic-example"
        sup.full_clean()

    def validWebsiteComplex2(self):
        """Try and submit supervisor with a complex (and security flawed) but
        valid website URL

        This should pass
        """
        sup = Supervisor()
        sup.first_name = "Arthur"
        sup.last_name = "Anderson"
        sup.email = "arthur.anderson@andersons.com"
        sup.website = "https://example.com?user=arthur&password=arthurspassword"
        sup.full_clean()
