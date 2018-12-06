from django.test import TestCase
from django.contrib.auth.models import User
from ff2ksite.models import Story, Chapter, Tags, Fandom, Categories, Profile

class FF2kTestCase(TestCase):
    fixtures = ['sites.json', 'users.json', 'fandoms.json', 'data.json'] 
    def setUp(self):
        self.user = User.objects.create_user(username='Testinator', password='mE4OvEmXT7rT5OZQTet00eQB', email='testinator@fail4free.de')

    def test_login(self):
        login = self.client.login(username='Testinator', password='mE4OvEmXT7rT5OZQTet00eQB')
