from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup , name="signup"),
    path('signin/', views.signin , name="signin"),
    path('create_task/', views.create_task , name="create_task"),
    path('view_task', views.view_task , name="view_task"),
    
]