from django.conf.urls import include, url
from django.contrib import admin
from odonto.views import *
from loginWebservice.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getLoginWebservice/', getLoginWebservice)
]
