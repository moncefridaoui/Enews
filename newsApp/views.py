from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def News(request):
    news = Article.objects.all()

    return render(request, 'newsApp/News.html', {
        'news': news
    })