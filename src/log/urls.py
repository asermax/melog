from django.conf.urls import patterns, url, include
from django.views import generic

import tastypie.api

from . import api as resources

api = tastypie.api.Api(api_name='v1')
api.register(resources.UserResource())
api.register(resources.LogResource())

urlpatterns = patterns(
    'log.views',
    url(r'^api/', include(api.urls)),
    url(r'^feed/?$',
        generic.TemplateView.as_view(template_name='log/feed.html')),
)
