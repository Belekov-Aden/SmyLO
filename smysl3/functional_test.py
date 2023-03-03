from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstall(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_init(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Site Belekov Aden', self.browser.title)

    def test_header(self):
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Belekov Aden', header)


if __name__ == '__main__':
    unittest.main()