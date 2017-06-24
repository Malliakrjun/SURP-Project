from django.contrib import admin
from .models import spark
from .models import Tag

# Register your models here.

admin.site.register(spark)
admin.site.register(Tag)