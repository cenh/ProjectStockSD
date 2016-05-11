from django.test import TestCase
from django.core.urlresolvers import reverse

class TestViews(TestCase):
    def test_index_list_view(self):
        """Test whether a request to the start page (index) is successful"""
        response = self.client.get(reverse('index'))

        self.assertTrue(200 <= response.status_code < 400)

    def test_group_list_view(self):
        """Test whether a request to the group page is successful"""
        response = self.client.get(reverse('group'))

        self.assertTrue(200 <= response.status_code < 400)

    def test_project_list_view(self):
        """Test whether a request to the project page is successful"""
        response = self.client.get(reverse('project'))

        self.assertTrue(200 <= response.status_code < 400)

    def test_supervisor_list_view(self):
        """Test whether a request to the supervisor page is successful"""
        response = self.client.get(reverse('supervisor'))

        self.assertTrue(200 <= response.status_code < 400)

    def test_admin_list_view(self):
        """Test whether a request to the admin index page is successful"""
        response = self.client.get(reverse('admin:index'))

        self.assertTrue(200 <= response.status_code < 400)
