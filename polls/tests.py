from datetime import datetime
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
import pytest
from .views import QuestionView
from .models import Question, Choice


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@email.com', password='top_secret')

    def test_question_view_empty_list(self):
        # Create an instance of a GET request.
        request = self.factory.get('/questions')
        view = QuestionView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_question_view_list(self):
        Question.objects.create(
            question_text='What is your name?', pub_date=datetime.now())
        request = self.factory.get('/questions')
        view = QuestionView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


@pytest.mark.parametrize("question_text, pub_date, validity", [
    ('What is your name?', datetime.now(), True),
    (None, datetime.now(), False),
    ('What is your name?', None, False),
],)
@pytest.mark.django_db
def test_question_create(question_factory, question_text, pub_date, validity):
    try:
        test = question_factory(question_text=question_text, pub_date=pub_date)
        item = Question.objects.all().count()
        assert item == validity
    except Exception as e:
        assert False == validity


@pytest.mark.django_db
def test_choice_create(question_factory, choice_factory):
    question = question_factory()
    choice1 = choice_factory(question=question)
    choice2 = choice_factory(question=question)
    item = Choice.objects.all().count()
    print(item)
    assert item == 2
    assert choice2.question == choice1.question
