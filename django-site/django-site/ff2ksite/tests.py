from django.test import TestCase
from django.contrib.auth.models import User
from ff2ksite.models import Story, Chapter, Tags, Fandom, Categories, Profile


class FF2kTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.fandom = Fandom.objects.create(fandom_name='Harry Potter', fandom_descr='Harry Potter fandom refers to the community of fans of the Harry Potter books and movies who participate in entertainment activities that revolve around the series, such as reading and writing fan fiction, creating and soliciting fan art...', fandom_short='HP')


    def test_animals_can_speak(self):
        login = self.client.login(username='testuser', password='12345')

