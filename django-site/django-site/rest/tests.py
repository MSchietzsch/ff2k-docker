from django.test import TestCase
import json

# Create your tests here.

# thought process:
#
# class FF2kresttest(RestTest):
#     fixtures = ['sites.json', 'users.json', 'fandoms.json', 'data.json'] 
#     def setUp(self):
#         self.user = User.objects.create_user(username='Testinator', password='mE4OvEmXT7rT5OZQTet00eQB', email='testinator@fail4free.de')
# 
#     def test_login(self):
#         login = self.client.login(username='Testinator', password='mE4OvEmXT7rT5OZQTet00eQB')
# 
#     def test_json_response(self):
#         response = client.get('/rest/stories/bc14ae1f/', content_type='application/json')
#         response.json()['story_title']

# TO DO tests:
#
# json get details of save story -> true
# json get details of UNsave story (unauthetificated) -> false
# json get details of UNsave story (authetificated) -> ture
# json get details of UNpublished story -> false
# json get userdetails (email) only authetificated -> true
# json get userdetails (email) unthetificated -> false
#



