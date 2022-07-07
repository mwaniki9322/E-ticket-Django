
from asyncio import events
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Event
from tickets.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def store(request,category_slug=None):
    categories=None
    events=None

    if category_slug !=None:
        categories=get_object_or_404(Category,slug=category_slug)
        events=Event.objects.filter(category=categories)
        paginator=Paginator(events,2)
        page=request.GET.get('page')
        paged_events=paginator.get_page(page)
        events_count=events.count()
    else:
        events=Event.objects.all().order_by('-id')
        paginator=Paginator(events,6)
        page=request.GET.get('page')
        paged_events=paginator.get_page(page)
        events_count=events.count()
    context={
        'events':paged_events,
        'events_count':events_count
        }

    return render(request,'./store/store.html',context)

def event_detail(request,category_slug,event_slug):
    
    try:
        single_event = Event.objects.get(category__slug=category_slug, slug=event_slug)
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),event=single_event).exists()
       
    except Exception as e:
        raise e
    context={
        'single_event':single_event,
        'in_cart':in_cart
    }
    return render(request,'./store/event_detail.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            events = Event.objects.order_by('-id').filter(event_description__icontains=keyword,event_name__icontains=keyword)
            events_count=events.count()
    context = {
        'events': events,
        'events_count':events_count,
    }
    return render(request, 'store/store.html', context)