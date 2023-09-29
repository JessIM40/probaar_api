from django.contrib import admin
from .models import Article

# Register your models here.

# Añadir campo publication_date para visualizar en panel admin
class ArticleAdmin(admin.ModelAdmin):
  readonly_fields = ("publication_date", ) 

# Visualizar mi app articles en el panel de admin
admin.site.register(Article, ArticleAdmin)