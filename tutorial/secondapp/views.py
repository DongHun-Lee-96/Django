from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital


def hospital(request):
    search = request.GET.get('search')
    if not search:
        search = ''

    hospital = Hospital.objects.filter(name__contains=search)
    #hospital = Hospital.objects.all()

    context = {'hospital': hospital}  # 앞의 'hospital'은 key 값
    return render(request, 'secondapp/hospital.html', context)
    # html = ''
    # for h in hospital:
    #     html += h.name + '<br>'
    # return HttpResponse(html)
