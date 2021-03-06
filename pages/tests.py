from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomepageTests(SimpleTestCase):
    """Docstring for the class."""

    def test_url_exists_at_correct_location(self):
        """Docstring for the function."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Docstring for the function."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Docstring for the function."""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """Docstring for the function."""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Home page</h1>")


class AboutpageTests(SimpleTestCase):
    """Docstring for the class."""

    def test_url_exists_at_correct_location(self):
        """Docstring for the function."""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Docstring for the function."""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Docstring for the function."""
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        """Docstring for the function."""
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
