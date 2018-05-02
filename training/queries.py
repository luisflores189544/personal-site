from django.core import serializers

from .models import Assignment, Session, Question, Choices, Results, ResultDetails



def get_question_choice(question_id):

    choices = Choices.objects.select_related('question').filter(question_id=question_id)
    question_name = choices[0].question
    choices = serializers.serialize('json', choices)

    dataset = {'status': 'in_progress', 'question':question_name}
    dataset['choices'] = choices

    return dataset 

def is_answer_correct(question_id, choice_id):
    answer = Choices.objects.get(question_id=question_id, choices_id=choice_id)   
    is_correct = answer.anwser

    return is_correct
        
def log_results(assignment_id):
    try:
        result = Results.objects.get(assignment_id=assignment_id)
        result.score += 1
        result.save()
    except:
        result_model = Results(assignment_id=assignment_id, score=1)
        result_model.save()

def insert_results_detail(assignment_id, question_id, correct):
    result_details = ResultDetails(assignment_id=assignment_id, 
            question_id=question_id, is_correct=correct)
    result_details.save()
    
def get_score(assignment_id, with_completed_date=None):
    score = Results.objects.get(assignment_id=assignment_id)
    if score.score < .70:
        pass_fail = 'FAIL'
    else:
        pass_fail = 'PASS'
    if with_completed_date == True:
        return "{0:.0f}%".format(score.score * 100), pass_fail, score.completed_date
    else:
        return "{0:.0f}%".format(score.score * 100), pass_fail

def calc_score(assignment_id):
    result_detail = ResultDetails.objects.filter(assignment_id=assignment_id)
    correct_answer = result_detail.filter(is_correct=True).count()
    total_question = result_detail.count()

    results = Results(score=correct_answer/total_question, assignment_id=assignment_id)
    results.save()

def update_assignment_status(assignment_id):
    assignment = Assignment.objects.get(assignment_id=assignment_id)
    assignment.status = 'COMPLETE'
    assignment.save()
        
def get_completed_assignments(user_id):
    assignments = Assignment.objects.prefetch_related('session').filter(user_id=user_id, status='COMPLETE')

    return assignments