from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from api_squid import views

urlpatterns = patterns('',
                       url(r'^api_squid/', include('api_squid.urls'))
                       )

