from django.contrib import admin
from .models import event,Event_Comment
# Register your models here.
admin.site.register(event)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'event', 'created', 'active')
    list_filter = ('active', 'created',)
    search_fields = ('author', 'body')
admin.site.register(Event_Comment,CommentAdmin)