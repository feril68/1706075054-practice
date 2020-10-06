from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page, get_lucky_number


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>pmpl feril</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_html_return_text_muhammad_feril_bagus_p(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertIn('<p class="text_full_name">muhammad feril bagus p</p>', html)

    def test_get_lucky_number_return_integer_object(self):
        lucky_number = get_lucky_number()
        self.assertEqual(type(lucky_number), int)
    
    def test_get_lucky_number_not_return_float_object(self):
        lucky_number = get_lucky_number()
        self.assertNotEqual(type(lucky_number), float)
    
    def test_home_page_context_contain_lucky_number(self):
        response = self.client.get("")
        lucky_number = response.context["lucky_number"]
        self.assertEqual(type(lucky_number), int)
