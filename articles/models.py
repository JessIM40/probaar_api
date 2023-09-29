from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  publication_date = models.DateTimeField(auto_now_add=True)
  
  # Visualizar en panel admin el texto real de los articulos
  def __str__(self):
    return self.title