from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.latest_news,name='latest_news'),
]