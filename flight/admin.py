from django.contrib import admin
from .models import Flight,Passenger,Rezervation
# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Rezervation)