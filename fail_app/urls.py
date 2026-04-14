from django.urls import path
from .views import *

app_name = 'fail_app'

urlpatterns = [
    path('', index, name='index'),
    path('result/', result, name='result'),
]