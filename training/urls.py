from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

app_name = 'training'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.home,
        name='home'
    ),
    url(
        regex=r'^(?P<assignment_id>[0-9a-f-]+)$',
        view=views.assignment,
        name='assignment'
    ),
    url(
        regex=r'^(?P<assignment_id>[0-9a-f-]+)/(?P<question_id>[0-9]+)$',
        view=views.question,
        name='question'
    ),
    url(
        regex=r'^(?P<assignment_id>[0-9a-f-]+)/results$',
        view=views.results,
        name='results'
    ),
    url(
        regex=r'^completed-list$',
        view=TemplateView.as_view(template_name='training/completed_list.html'),
        name='completed'
    )

	]