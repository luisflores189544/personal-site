from django import template
# from django.db.models import Prefetch

from training.models import Assignment, Session
from training.queries import get_completed_assignments, get_score

import datetime
import markdown2
import os

register = template.Library()

@register.simple_tag
def get_required_training(user_id):

    assignment = Assignment.objects.prefetch_related('session').filter(user_id=user_id, status='OPEN')
    data = []
    for session in assignment:
        if session.session.due_date >= datetime.date.today():
            data.append({'title':session.session.title, 
                'due_date':str(session.session.due_date),
                'id': str(session.assignment_id)})
    return data


@register.simple_tag
def get_past_due_training(user_id):
    
    assignment = Assignment.objects.prefetch_related('session').filter(user_id=user_id, status='OPEN')
    data = []
    for session in assignment:
        if session.session.due_date < datetime.date.today():
            data.append({'title':session.session.title, 
                'due_date':str(session.session.due_date),
                'id': str(session.assignment_id)})
    return data


@register.simple_tag
def get_completed_training(user_id):
    assignments = get_completed_assignments(user_id)
    data = []
    for session in assignments:
        score, session_status, completed_date = get_score(session.assignment_id, True)
        data.append({'title':session.session.title,
            'status': session.status, 'score':score,
            'completed_date': str(completed_date),
            'session_status': session_status})
    return data