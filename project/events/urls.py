from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^profile/(?P<pk>\d+)/$',views.profile,name='profile'),
    url(r'^add-event/$', views.add, name='add-event'),
    url(r'^$', views.events, name='events'),
    url(r'^attend/(?P<pk>\d+)/(?P<pk2>\d+)/$',views.attend,name='attending')
]