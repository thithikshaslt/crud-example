from django.contrib import admin

from .models import Stage_Event,Show,Ticket

# Register your models here.
admin.site.register(Stage_Event)
admin.site.register(Show)
admin.site.register(Ticket)
