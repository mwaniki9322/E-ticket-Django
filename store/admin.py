from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('event_name',)}
    list_display=('event_name','slug')


admin.site.register(Event,EventAdmin)
