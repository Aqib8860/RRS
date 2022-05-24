from django.urls import path
from resturent.views import *


app_name = 'resturent'

urlpatterns = [
    path('add-resturent/', AddResturentView.as_view(), name='add-resturent'),

]
