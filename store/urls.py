from django.urls import path
from . import views

urlpatterns=[
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='events_by_category'),
    path('<slug:category_slug>/<event_slug>/',views.event_detai,name='events_detail')
]