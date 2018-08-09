from django.urls import path
from . import views
# http://127.0.0.1:8000/hello/my_name_is_taromorita.I_am_38_years_old.
urlpatterns = [
        path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.index, name='index'),
]
