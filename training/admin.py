from django.contrib import admin
from .models import *

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id','title', 'due_date',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ('choice', 'anwser', 'seq',)

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'user_id', 'status',)

class ResultsAdmin(admin.ModelAdmin):
    list_display = ('score', 'completed_date', 'assignment_id',)

admin.site.register(Session, SessionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Results, ResultsAdmin)