from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.ad),    
    path('stories/chapter/new', views.story_new),
    re_path('(?P<auto_uid>[a-fA-F0-9]{8})/?$', views.ad_story_detail),
]
