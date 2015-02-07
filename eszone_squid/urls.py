from django.conf.urls import patterns, include, url
from django.contrib import admin

from api_squid import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^acl_rules/(?P<pk>\d+)/$', views.acl_rule_detail, name='acl_rule_detail'),
                       url(r'^acl_rules/$', views.acl_rules_list, name='acl_rules_list'),
                       # http_access
                       # url(r'^acl_list/$', views.acl_list, name='acl_list'),
                       )

