from django.test import TestCase
from django.urls import reverse
from article.models import Categorie, Article

class HomeTestCase(TestCase):
    def setUp(self):
        Categorie.objects.create(nom="A la une", status="Active")
        Article.objects.create(titre="Test", contenu="Contenu du test", categorie=Categorie.objects.get(nom="A la une"))

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(len(response.context['categories']), 1)

class DetailsTestCase(TestCase):
    def setUp(self):
        Categorie.objects.create(nom="A la une", status="Active")
        Article.objects.create(titre="Test", contenu="Contenu du test", categorie=Categorie.objects.get(nom="A la une"))

    def test_details(self):
        response = details(None, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['article'].titre, "Test")