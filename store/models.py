from django.urls import reverse
from django.db import models
from tickets.models import Category

# Create your models here.

class Event(models.Model):
    event_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    event_description=models.TextField(max_length=500,blank=True)
    event_venue=models.CharField(max_length=100)
    event_date=models.CharField(max_length=100)
    event_time=models.CharField(max_length=100)
    event_image=models.ImageField(default='media/default.svg')
    event_price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('events_detail',args=[self.category.slug,self.slug])

    def __str__(self):
       return self.event_name
