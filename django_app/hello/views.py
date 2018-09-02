from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm
# http://127.0.0.1:8000/hello/my_name_is_taromorita.I_am_38_years_old.

def index(request):
    data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'message': 'all friends',
            'form': HelloForm(),
            'data': data,
        }
    if (request.method == 'POST'):
        num=request.POST['id']
        item= Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
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
