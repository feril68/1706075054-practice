from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_web_title_is_pmpl_feril(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('pmpl feril', self.browser.title)
    
    def test_text_muhammad_feril_bagus_p_is_displayed(self):
        self.browser.get('http://localhost:8000')
        full_name = self.browser.find_element_by_class_name("text_full_name").text
        self.assertEqual("muhammad feril bagus p", full_name)

    def test_text_lucky_number_is_displayed(self):
        self.browser.get('http://localhost:8000')
        lucky_number = self.browser.find_element_by_class_name("text_lucky_number").text
        self.assertNotEqual(lucky_number.find("lucky number (random) :"), -1)

    def test_integer_lucky_number_is_displayed(self):
        self.browser.get('http://localhost:8000')
        lucky_number_text = self.browser.find_element_by_class_name("text_lucky_number").text
        number = int(lucky_number_text.split(" ")[-1])
        self.assertEqual(type(number), int)

if __name__ == '__main__':
    unittest.main()