from django.shortcuts import render, render_to_response, redirect, resolve_url, reverse
from django.urls import reverse as reverse_http
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages, sessions
from django.template.context_processors import csrf


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('training:home'))
    
    elif request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('training:home'))
        else:
            message = 'Invalid! Reenter User Name and/or Password.'
            alert_type = 'danger'
            return TemplateResponse(request, 'login/login.html', {'message':message, 'alert_type':alert_type})
    
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('login/login.html', c)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))