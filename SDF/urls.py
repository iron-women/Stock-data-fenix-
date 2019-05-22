from django.urls import path
from SDF.views import *

app_name = 'sdf'

urlpatterns = [
    path('login/', show_log, name='log'),
    path('register/', show_reg, name='reg'),
    path('index/', show_index, name='index'),
]