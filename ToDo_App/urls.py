from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='ToDo_App'
urlpatterns=[
    #Home Page
    path('', views.index, name='index'),
    path('new_list/', views.new_list, name='new_list'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)