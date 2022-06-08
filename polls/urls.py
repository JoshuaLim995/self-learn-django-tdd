from django.urls import path

from . import views

urlpatterns = [
    path('questions', views.QuestionView.as_view(), name='questions'),
]
