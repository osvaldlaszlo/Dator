"""ruenoor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tastypie.api import Api
from robots.api import *
from robots.views import simple_view, root_view

#admin.autodiscover()

# tasty-pie definitions
v1_api = Api(api_name='v1')

# equipment resources
v1_api.register(SystemResource())
v1_api.register(ProgramResource())
v1_api.register(LocalComputerResource())

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^ruenoor/', simple_view, name='SimpleURL'),
    url(r'^$', root_view, name='RootView')
]
