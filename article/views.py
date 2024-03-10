from django.shortcuts import render

def home(request):
  
    return render(request, 'article/index.html')

def details(request, pk):
    #commande = Commande.objects.get(id=pk)
    #context = {'commande':commande}
    return render(request, 'article/details.html')