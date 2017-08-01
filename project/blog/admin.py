# from django.contrib import admin
# from .models import Post
# # Register your models here.
# admin.site.register(Post)

from django.contrib import admin
from .models import Post,Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created','status')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['status', 'created']
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'active')
    list_filter = ('active', 'created',)
    search_fields = ('author', 'body')
admin.site.register(Comment,CommentAdmin)