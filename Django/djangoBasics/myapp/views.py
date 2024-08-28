from django.shortcuts import render, redirect
from django.http import HttpResponse

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoBasics.settings')
from .models import Article, Author



# Create your views here.


def welcome(request):
    # return HttpResponse('Welcome To My APP! Powered By Omar Mohamed Sharawi.')
    return render(request, 'index.html', {
        'name': 'Omar Mohamed Sharawi',
        'categorise': [
            'catg1',
            'catg2',
            'catg3'
        ],
        'test': 'test to upper first char'
    })


# def showarticle(request, id, slug):
#     # return HttpResponse('Article ' + str(id) + ' ' + str(slug))
#     return render(request, 'articles/showArticle.html', {
#         'title': 'Article ' + str(id),
#         'content': ' ' + str(slug)
#     })


def home(request):
    # method to add data in database
    # author = Author()
    # author.name = 'Omar'
    # author.email = 'omarmosharawi@gmail.com'
    # author.save()

    # another method to add data
    # Author.objects.create(name='Mohamed', email='mohamed@example.com')

    # add data in article
    # article = Article()
    # article.author = Author(1)
    # article.title = 'Python 3.14'
    # article.content = 'this content here ...'
    # article.save()

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def showArticles(request):
    models = Article.objects.select_related('author').all()[:10]  # return all objects # using [:10] to print first 10 values
    # using select_related() to reduce sql query in one to one relation
    # using prefetch_related() in one to many or many to many

    # models = Article.objects.filter(pk__range=(10, 20))
    # models = Article.objects.filter(title__contains='Python')   # '__contains' = 'LIKE' in DataBase
    # models = Article.objects.filter(title__icontains='python')   # '__icontains' = 'LIKE' in DataBase
    # models = Article.objects.filter(title__startwith='python')

    # models = Article.objects.get(pk=id)  # return unique one object # id must be a parameter in function

    # models = Article.objects.filter(pk=id)  # returns a collection of objects that match a specified condition
    # models = Article.objects.first(pk=id)  # returns the first object matching the specified conditions, or 'None' if it does not exist
    # models = Article.objects.filter(pk=id).update(title='New Title')  # update object value in database

    return render(request, 'articles/showArticle.html', {
        'articles': models
    })


# def delArticle(request, pk):
#     article = Article.objects.get(pk=pk)
#     article.delete()
#
#     Article.objects.filter(pk__gt=1).delete()   # gt = greater than
#     Article.objects.all().delete()
#     return redirect('/myapp/articles/showArticle.html')