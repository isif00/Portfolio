from django.test import TestCase
from .models import Projects


# Create your tests here.
class ProjectTestCase(TestCase):
    def testProject(self):
        post = Projects(title="My project", description="my project is cool !", link="https://www.google.com")
        self.assertEqual(post.title, "My project")
        self.assertEqual(post.description, "my project is cool !")
        self.assertEqual(post.link, "https://www.google.com")

