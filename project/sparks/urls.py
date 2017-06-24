from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/(?P<pk>\d+)/$',views.profile,name='profile'),
    url(r'^success/$', views.success, name='success'),
]