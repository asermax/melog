from django.contrib import auth
from tastypie import resources, authentication, authorization, fields

from . import models


class UserResource(resources.ModelResource):
    class Meta:
        queryset = auth.models.User.objects.all()
        resource_name = 'user'
        fields = ['id']
        allowed_methods = ['get']
        authentication = authentication.SessionAuthentication()
        authorization = authorization.ReadOnlyAuthorization()


class LogResource(resources.ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = models.Log.objects.all()
        resource_name = 'log'
        always_return_data = True
        authentication = authentication.SessionAuthentication()
