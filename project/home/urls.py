from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.homepage,name='home'),
    url(r'^malnutrition/$',views.malnutrition,name='malnutrition'),
    url(r'^education/$',views.education,name='education'),
    url(r'^poverty/$',views.poverty,name='poverty'),
    url(r'^social_welfare/$',views.social,name='social'),
    url(r'^hygiene/$',views.hygiene,name='hygiene'),
    url(r'^all-sparks/$',views.all_sparks,name='all_sparks'),
]