from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice

# urls.py 내에서 question_id라는 명칭을 사용했기 때문에


def reset(request, question_id):
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()
    for choice in choices:  # for-each
        choice.votes = 0
        choice.save()

    return redirect('/polls/'+str(question_id))
    # return redirect('/polls/%s' % question_id)


def vote(request, question_id):
    # 사용자가 선택한 radio 값
    choice_id = request.GET.get('choice')
    # ORM 에서는 primary key 값이 존재하면 update 코드가 수행
    # Choice(id=choice_id) (X)
    choice = Choice.objects.get(id=choice_id)
    choice.votes = choice.votes+1
    choice.save()  # update

    return redirect('/polls/')


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def index(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse('Hello, you are at the polls index')
