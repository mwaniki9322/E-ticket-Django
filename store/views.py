from django.shortcuts import get_object_or_404, render
from .models import Event
from tickets.models import Category

# Create your views here.

def store(request,category_slug=None):
    categories=None
    events=None

    if category_slug !=None:
        categories=get_object_or_404(Category,slug=category_slug)
        events=Event.objects.filter(category=categories)
        events_count=events.count()
    else:
        events=Event.objects.all()
        events_count=events.count()
    context={
        'events':events,
        'events_count':events_count
        }

    return render(request,'./store/store.html',context)

def event_detai(request,category_slug,event_slug):
    
    try:
        single_event = Event.objects.get(category__slug=category_slug, slug=event_slug)
    except Exception as e:
        raise e
    context={
        'single_event':single_event
    }
    return render(request,'./store/event_detail.html',context)