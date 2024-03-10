from django.shortcuts import render
from .models import Categorie,Article

def home(request):
    categories = Categorie.objects.get(nom="A la une" , status="Active")
    toutes_categories = Categorie.objects.filter(status="Active").exclude(nom="A la une")
    context = {
        "categories": categories,
        "toutes_categories": toutes_categories
    }
    return render(request, 'article/index.html', context=context)

def details(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article": article
    }
    return render(request, 'article/details.html', context=context)