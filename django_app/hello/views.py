from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
# http://127.0.0.1:8000/hello/my_name_is_taromorita.I_am_38_years_old.

def index(request):
    data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'message': 'all friends',
            'data': data,
        }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
            'title': 'Hello/Next',
            'msg': 'これは、もう一つのページです',
            'goto': 'index',
        }
    return render(request, 'hello/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
            'title': 'Hello/Form',
            'msg': 'こんにちは、 ' + msg + 'さん',
            }
    return render(request, 'hello/index.html', params)
