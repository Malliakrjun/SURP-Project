from django.db import models
import requests
from bs4 import BeautifulSoup
# Create your models here.

class news(models.Model):
    url=models.URLField(max_length=200)
    title=models.TextField()
