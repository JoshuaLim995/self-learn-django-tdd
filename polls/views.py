from django.http import HttpResponse
from rest_framework import generics

from polls.serializers import QuestionSerializer
from .models import Question, Choice


class QuestionView(generics.ListCreateAPIView):

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()
