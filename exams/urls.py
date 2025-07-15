from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('exam/<int:pk>/', views.take_exam, name='take_exam'),
    path('exam/<int:pk>/submit/', views.submit_exam, name='submit_exam'),
    path('results/', views.my_results, name='results'),
    path('register/', views.register, name='register'),
]