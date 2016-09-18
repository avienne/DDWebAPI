from django.conf.urls import include, url
from app import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', DDWebAPI.views.home, name='home'),
    url(r'getCharacter', views.get_character, name='getCharacter')
]
