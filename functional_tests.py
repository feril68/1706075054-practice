from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
      table = self.browser.find_element_by_id('id_list_table')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn(row_text, [row.text for row in rows])

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

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('TO-DO', self.browser.title)
        header_text = self.browser.find_element_by_id('h1_to_do').text  
        self.assertIn('TO-DO', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')  

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            f"New to-do item did not appear in table. Contents were:\n{table.text}"
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()