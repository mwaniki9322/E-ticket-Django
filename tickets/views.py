from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Event

# Create your views here.

def home(request):
    events=Event.objects.all()[:6]

    context={
        'events':events
    }
    return render(request,'home.html',context)
