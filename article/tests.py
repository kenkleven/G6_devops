from django.test import TestCase
from django.urls import reverse
from .models import Categorie, Article
from .views import home, details
from django.core.files.uploadedfile import SimpleUploadedFile

def setUp(self):
    self.categorie = Categorie.objects.create(nom='A la une', status='Active')
    image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
    self.article = Article.objects.create(nom='Mon article', description='Description de l\'article', status='Actif', categorie=self.categorie, image=image)

    def test_home_view(self):
        response = self.client.get(reverse('accueil'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/index.html')
        self.assertContains(response, 'A la une')
        self.assertContains(response, 'Mon article')

    def test_details_view(self):
        response = self.client.get(reverse('details', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/details.html')
        self.assertContains(response, 'Mon article')
        self.assertContains(response, 'Description de l\'article')
