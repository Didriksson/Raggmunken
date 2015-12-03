#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _
import re

from RaggmunkenApp.models import FoodItem
from models import FoodItem


class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
    
class FoodItemForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(FoodItemForm, self).__init__(*args, **kwargs)
        self.fields['matatttabort'] = forms.MultipleChoiceField(required=False,label=u'Mat du övervakar:', choices=[ (o.id, o.food) for o in FoodItem.objects.filter(username=user)], widget=forms.CheckboxSelectMultiple())        
        self.fields['matatttlaggatill'] = forms.CharField(required=False, label=u'Lägg till mat',widget=forms.TextInput(attrs=dict(required=False, max_length=30)))
    
        
        
        
        
        
        
        
        
        
        
        
        