from django.urls import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=255)
    cat_image=models.ImageField(default='media/default.svg')

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('events_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name
