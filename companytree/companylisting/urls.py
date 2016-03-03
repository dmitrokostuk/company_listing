
from django.conf.urls import url
from django.contrib import admin

from .views import (
    company_create,
    company_edit,
    company_list,
    company_delete,
    company_detail,

	)

urlpatterns = [
	url(r'^$', company_list ,name='company'),
    url(r'^create/$', company_create, name='create'),
    url(r'^(?P<id>\d+)/$',company_detail , name='detail'),

    url(r'^(?P<id>\d+)/edit/$', company_edit, name='edit'),
    url(r'^(?P<id>\d+)/delete/$', company_delete, name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]