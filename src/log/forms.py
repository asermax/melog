from django import forms
from django.utils.translation import ugettext as _ 

from . import models


class LogForm(forms.ModelForm):
    class Meta:
        model = models.Log
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(LogForm, self).__init__(*args, **kwargs)

        self.fields['text'].error_messages = {
            'required': _("The log can't be empty")
        }
