from django.urls import path
from . import views
# http://127.0.0.1:8000/hello/my_name_is_taromorita.I_am_38_years_old.
urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name='next'),
    path('form', views.form, name='form'),
]
