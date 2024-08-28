from django.urls import path
from . import views


urlpatterns = [
    path('welcome/', views.welcome),
    # path('article/<int:id>/<slug:slug>', views.showarticle),
    path('home/', views.home),
    path('about/', views.about),
    path('showarticles/', views.showArticles),
    # path('deletearticle/', views.delArticle),
]