"""
Definition of urls for DDWebAPI.
"""
from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.authtoken import views
import app.urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', DDWebAPI.views.home, name='home'),
    # url(r'^DDWebAPI/', include('DDWebAPI.DDWebAPI.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(app.urls)),
    url(r'^api-auth/', views.obtain_auth_token)
]
