from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile),
    path('p/<username>/', views.profile_other),
    re_path('f/(?P<fandom_short>[a-zA-Z0-9]+)/$', views.fandom),
    re_path('read/(?P<auto_uid>[a-fA-F0-9]{8})/?$', views.detail),
    re_path('read/(?P<auto_uid>[a-fA-F0-9]{8})/(?P<chapter_number>[0-9])/?$', views.chapter_view),
    path('search/', views.search),
    path('about/', views.about),
    path('privacy/', views.privacy),
    path('disclaimer/', views.disclaimer),
    path('messages/', include("pinax.messages.urls", namespace="pinax_messages")),

### termsfeed.com
# Privacy Policy
# Terms and Conditions
# Cookies Policy

]
