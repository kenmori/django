from django.shortcuts import render
from django.http import HttpResponse
# http://127.0.0.1:8000/hello/my_name_is_taromorita.I_am_38_years_old.

def index(request):
    params = {
            'title': 'Hello/Index',
            'msg': 'これは、サンプルで作ったページです',
        }
    return render(request, 'hello/index.html', params)
