from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="list"),
    path('updatetodo/<str:pk>/', views.update, name='updatetodo'),
    path('deletetodo/<str:pk>/', views.deleteTask, name='deletetodo'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]
