from django.contrib import admin

from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(UserProfile, UserProfileAdmin)


class HotelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'city']
    list_display = ['name', 'star', 'price', 'city']


admin.site.register(Hotel, HotelAdmin)

