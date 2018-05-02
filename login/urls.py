from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'login'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.login,
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view=views.logout,
        name='logout'
    ),
	]