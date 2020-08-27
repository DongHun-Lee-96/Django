from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from article.models import User
import hashlib


def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(email=email, pwd=pwd)
            request.session['email'] = email
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        # 회원정보 저장
        email = request.POST.get('email')
        name = request.POST.get('name')

        pwd = request.POST.get('pwd')
       # m = hashlib.sha256()
       # m.update(bytes(pwd, encoding='utf-8'))
       # pwd = m.hexdigest()

        user = User(email=email, name=name, pwd=pwd)
        user.save()
        return HttpResponseRedirect('/index/')
    return render(request, 'signup.html')


def index(request):
    return render(request, 'index.html')
