from . import views
from django.urls import path

urlpatterns = [
    # path('post-info', views.query_to_json, name='post-info'),
    path('stu-info/', views.query_to_json, name='stu-info'),

    
] 
