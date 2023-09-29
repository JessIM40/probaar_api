# from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from articles import views

# Generamos las rutas GET, POST, PUT, DELETE 
router = routers.DefaultRouter()
router.register(r'articles', views.ArticleView, 'articles')

# versionado de api
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Articles API')),
]
