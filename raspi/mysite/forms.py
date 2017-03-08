#_*_ coding: utf-8 _*_
from django.forms import ModelForm
from mysite import models

class SubdomainForm(ModelForm):
    class Meta:
        model = models.Subdomain
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(SubdomainForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '網址ID'
