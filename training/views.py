from django.shortcuts import render, reverse
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Assignment, Session, Question, Choices
from .queries import get_question_choice, is_answer_correct, log_results, get_score, insert_results_detail, calc_score, update_assignment_status

def home(request):  
    if request.user.is_authenticated:
        return TemplateResponse(request, 'training/home.html')
    else:
        return redirect_to_home(request)

def assignment(request, assignment_id):
    if request.user.is_authenticated:
        try:
            assignment = Assignment.objects.get(assignment_id=assignment_id, user_id=request.user.id)
        except Assignment.DoesNotExist:
            return redirect_to_training_home(request)

        question = Question.objects.select_related('session').filter(session_id=assignment.session_id).order_by('question_id')

        title = question[0].session
        first_question = '/'.join([str(assignment.assignment_id), str(question[0].question_id)])
        return TemplateResponse(request, 'training/training_session.html', {'title':title, 
                            'question':first_question})
    else:
        return redirect_to_home(request)

def question(request, assignment_id, question_id):
    if request.user.is_authenticated:
        question_data = Question.objects.select_related('session').get(question_id=question_id)
        title =  question_data.session
        
        if request.POST:
            answer = request.POST['selected_choice']  
            insert_results_detail(assignment_id, question_id, is_answer_correct(question_id, answer))

            assignment = Assignment.objects.get(assignment_id=assignment_id)
            
            questions = Question.objects.select_related('session').filter(session_id=assignment.session_id, 
                        question_id__gt=question_id).order_by('question_id')
            try:
                question = questions[0].question_id
            except:
                calc_score(assignment_id)
                update_assignment_status(assignment_id)
                return HttpResponseRedirect(reverse('training:results', args=(str(assignment_id),)))

            return HttpResponseRedirect(reverse('training:question', args=(str(assignment_id), str(question))))
        
        dataset = get_question_choice(question_id)
        dataset['title'] = title
        
        return TemplateResponse(request, 'training/training_session.html', dataset)
    else:
        return redirect_to_home(request)


def results(request, assignment_id):
    if request.user.is_authenticated:
        score_results, is_pass_fail = get_score(assignment_id)
        return TemplateResponse(request, 'training/training_results.html', {'score':score_results, 'is_pass_fail': is_pass_fail})
    else:
        return redirect_to_home(request)

# redirect user back to home page, when user is not authorized.
# prevent user from accessing pages via url manipulation.
def redirect_to_home(request):
    return HttpResponseRedirect(reverse('home'))

def redirect_to_training_home(request):
    return HttpResponseRedirect(reverse('training:home'))