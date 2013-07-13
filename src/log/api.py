from django.contrib import auth
from tastypie import resources, authentication, authorization, fields, \
    validation

from . import models, forms


class PerUserAuthorization(authorization.Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.user == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming their auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def delete_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user


class PerUserResource(resources.ModelResource):
    def obj_create(self, bundle, **kwargs):
        return super(PerUserResource, self).obj_create(
            bundle, user=bundle.request.user)


class UserResource(resources.ModelResource):
    class Meta:
        queryset = auth.models.User.objects.all()
        resource_name = 'user'
        fields = ['id']
        allowed_methods = ['get']
        authentication = authentication.SessionAuthentication()
        authorization = authorization.ReadOnlyAuthorization()


class LogResource(PerUserResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = models.Log.objects.all()
        resource_name = 'log'
        always_return_data = True
        authentication = authentication.SessionAuthentication()
        authorization = PerUserAuthorization()
        validation = validation.FormValidation(form_class=forms.LogForm)
