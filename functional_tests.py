from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from pyvirtualdisplay import Display
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # display = Display(visible=0, size=(800, 600))
        # display.start()
        #self.browser = webdriver.Chrome()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        # self.browser.get('http://localhost:8001')
        self.browser.get('http://127.0.0.1:8000')

        # She notices the page title and header mention to-do lists
        # title_text = self.browser.find_element(By.TAG_NAME,'title').text
        # time.sleep(1)
        # self.assertIn('To-Do', title_text )
        self.assertIn("To-Do", self.browser.title)
  
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        time.sleep(1)

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very
# methodical)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows], f"New to-do item did not appear in table. Contents were:\n{table.text}")
        self.assertIn('2: Use peacock feathers to make a fly',[row.text for row in rows], f"New to-do item did not appear in table. Contents were:\n{table.text}")
# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.
        self.fail('Finish the test!')
# She visits that URL - her to-do list is still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
