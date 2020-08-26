from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *


def show(request):
    curriculum = Curriculum.objects.all()
    context = {'curriculum': curriculum}
    return render(request, 'firstapp/show.html', context)
#     html = ''
#     for c in curriculum:
#         html += c.name + '<br>'
#     return HttpResponse(html)


def add(request):
    # 데이터베이스에 데이터 입력
    # 데이터 3개 insert into firstapp_curriculum
    c1 = Curriculum(name='python')
    c1.save()
    c2 = Curriculum(name='java')
    c2.save()
    c3 = Curriculum(name='spring')
    c3.save()
    return HttpResponse('OK')


def main(request):
    return HttpResponse('Main!!')


def index1(request):
    return HttpResponse('<h1>Hello</h1>')


def json(request):
    return JsonResponse({'key1': 'value1', 'key2': 'value2'})
    # XXXResponse
    # redirect
    # render
