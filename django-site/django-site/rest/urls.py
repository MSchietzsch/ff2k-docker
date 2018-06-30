from django.urls import path, include, re_path
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#router = routers.DefaultRouter()

urlpatterns = [
    #path('/', include('router.urls')),
    path('api-auth/', include('rest_framework.urls')),    
    path('stories/', views.rest_story_list.as_view()),
    re_path('stories/(?P<auto_uid>[a-fA-F0-9]{8})/?$', views.rest_story_detailas_view.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)