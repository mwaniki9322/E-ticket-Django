from re import search
from django.urls import path
from . import views

urlpatterns=[
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/',views.store,name='events_by_category'),
    path('category/<slug:category_slug>/<event_slug>/',views.event_detail,name='events_detail'),
    path('search/',views.search,name='search')
]