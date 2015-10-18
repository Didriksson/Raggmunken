#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
from django.http import HttpResponse
from django.contrib.auth.models import User
from forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView
from models import FoodItem
from RaggmunkenApp.forms import FoodItemForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world! This is the Raggmunken Index speaking.")

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    if request.method == 'POST':
        form = FoodItemForm(request.user, request.POST)
        if form.is_valid():
            matAttTaBort = form.cleaned_data.get('matatttabort')
            laggTillMat = form.cleaned_data.get('matatttlaggatill')
            
            if matAttTaBort:
                for food_id in matAttTaBort:
                    FoodItem.objects.get(id=food_id).delete()
            
            if laggTillMat:
                FoodItem.objects.create(username=request.user, food = laggTillMat)
                
                
    form = FoodItemForm(request.user)
    return render_to_response('home.html', {'form':form },
        context_instance=RequestContext(request))
