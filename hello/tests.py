from django.test import TestCase


class HelloWorldViewTests(TestCase):
	def test_hello_world_page_returns_greeting(self):
		response = self.client.get('/hello/')

		self.assertContains(response, 'Hello, World!')
