import pytz

from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from blog.views import home_page, article_page
from blog.models import Article
from datetime import datetime

class ArticlePageTest(TestCase):

    def test_article_display_article_correct(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdata=datetime.now().replace(tzinfo=pytz.utc),
            slug='slug-1'
        )

        request = HttpRequest()
        response = article_page(request, 'slug-1')
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('full_text 1', html)
        self.assertNotIn('summary 1', html)



class HomePageTest(TestCase):


    def test_home_page_display_articles(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdata=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1'
        )
        Article.objects.create(
            title='title 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdata=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2'
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('blog/slug-1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('blog/slug-2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('full_text 2', html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Site Belekov Aden</title>', html)
        self.assertIn('<h1>Belekov Aden</h1>', html)
        self.assertTrue(html.endswith('</html>'))


class ArticleModelTests(TestCase):

    def test_article_model_save_and_retrieve(self):
        article_one = Article(
            title='article 1',
            full_text='full text 1',
            summary='summary 1',
            category='category 1',
            pubdata=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-1',
        )
        article_one.save()

        article_two = Article(
            title='article 2',
            full_text='full text 2',
            summary='summary 2',
            category='category 2',
            pubdata=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug='slug-2',

        )
        article_two.save()

        all_articles = Article.objects.all()

        self.assertEqual(len(all_articles), 2)

        self.assertEqual(
            all_articles[0].title,
            article_one.title
        )

        self.assertEqual(
            all_articles[1].title,
            article_two.title
        )

        self.assertEqual(
            all_articles[0].slug,
            article_one.slug
        )

        self.assertEqual(
            all_articles[1].slug,
            article_two.slug
        )