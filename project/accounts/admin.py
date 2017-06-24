from django.contrib import admin
from accounts.models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','description')

# Register your models here.
admin.site.register(UserProfile)
admin.site.site_header='Administration'

