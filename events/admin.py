from django.contrib import admin
from . models import Registration, Event,CustomUser 
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(CustomUser, UserAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'created_by')
	search_fields = ('title',)
	list_filter = ('date',)

admin.site.register(Event, EventAdmin)	

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('user', 'event', 'registered_at')

admin.site.register(Registration, RegistrationAdmin)


