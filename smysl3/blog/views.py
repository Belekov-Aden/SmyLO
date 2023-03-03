from django.http import HttpResponse
from django.shortcuts import render
from .models import  Article

def home_page(request):
    articles = Article.objects.all()
    context = {'acticles': articles}
    return render(request, 'home_page.html', context)
