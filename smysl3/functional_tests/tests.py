import pytz
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime

class BasicInstall(LiveServerTestCase):

    def setUp(self):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        self.browser = webdriver.Firefox(options=option)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdata=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1'
        )

    def tearDown(self):
        self.browser.quit()

    def test_init(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Site Belekov Aden', self.browser.title)

    def test_header(self):
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Belekov Aden', header)

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue(header.location['x'] > 10)

    def test_home_page_blog(self):
        self.browser.get(self.live_server_url)
        arcticle_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(arcticle_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get(self.live_server_url)
        arcticle_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        arcticle_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(arcticle_title)
        self.assertTrue(arcticle_summary)


    def test_home_page_article_title_link_to_article_page(self):
        self.browser.get(self.live_server_url)
        arcticle_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        arcticle_title_text = arcticle_title.text
        arcticle_link = arcticle_title.find_element(By.TAG_NAME, 'a')

        self.browser.get(arcticle_link.get_attribute('href'))
        arcticle_title_article = self.browser.find_element(By.CLASS_NAME, 'article-title')

        self.assertEqual(arcticle_title_text, arcticle_title_article.text)