from django.test import TestCase
from project_stock.models import Group, Project, Publication, Supervisor
from django.core.exceptions import ValidationError

valid_urls = ['http://example.com',
              'https://docs.python.org/3/library/unittest.html#basic-example',
              'https://example.com?user=arthur&password=arthurspassword']

invalid_urls = ['invalidwebsite',
                'htt://example.com',
                'example.com']

class TestProject(TestCase):
    def test_create_no_attributes(self):
        """Try and create a project without setting any attributes

        This should fail with ValidationError
        """
        project = Project()
        with self.assertRaises(ValidationError):
            project.full_clean()

    def test_create_necessary_attributes(self):
        project = Project()
        project.name = 'Test project'
        project.type = 'O'
        project.full_clean()

    def test_valid_website(self):
        project = Project()
        project.name = 'Test project'
        project.type = 'O'
        for u in valid_urls:
            project.website = u
            project.full_clean()

    def test_invalid_website(self):
        project = Project()
        project.name = 'Test project'
        project.type = 'O'
        for u in invalid_urls:
            project.website = u
            with self.assertRaises(ValidationError):
                project.full_clean()

class TestSupervisor(TestCase):
    def test_create_no_attributes(self):
        """Try and create a supervisor without setting any attributes

        This should fail with ValidationError
        """
        supervisor = Supervisor()
        with self.assertRaises(ValidationError):
            supervisor.full_clean()

    def test_create_necessary_attributes(self):
        """Try and create a supervisor with the necessary attributes

        This should pass
        """
        supervisor = Supervisor()
        supervisor.first_name = 'Arthur'
        supervisor.last_name = 'Anderson'
        supervisor.email = 'arthur.anderson@andersons.com'
        supervisor.full_clean()

    def test_valid_websites(self):
        """Try and submit supervisor with various valid website URLs

        This should pass
        """
        supervisor = Supervisor()
        supervisor.first_name = 'Arthur'
        supervisor.last_name = 'Anderson'
        supervisor.email = 'arthur.anderson@andersons.com'
        for u in valid_urls:
            supervisor.website = u
            supervisor.full_clean()

    def test_invalid_websites(self):
        """Try and submit supervisor with an invalid website URL

        This should fail with ValidationError
        """
        supervisor = Supervisor()
        supervisor.first_name = 'Arthur'
        supervisor.last_name = 'Anderson'
        supervisor.email = 'arthur.anderson@andersons.com'
        for u in invalid_urls:
            supervisor.website = u
            with self.assertRaises(ValidationError):
                supervisor.full_clean()
