from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    # fields = ('id', 'title', 'content', 'publication_date',) # Seleccinando los campos a serializarse
    fields = '__all__' # Serializa todos los campos