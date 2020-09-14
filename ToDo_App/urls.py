from django.urls import path
from . import views

app_name='ToDo_App'
urlpatterns=[
    #Home Page
    path('', views.index, name='index'),
    path('new_list/', views.new_list, name='new_list'),
    
]