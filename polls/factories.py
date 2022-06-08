import factory
from faker import Faker
from . import models

faker = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Question

    question_text = faker.name()
    pub_date = faker.date_time()


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Choice

    choice_text = faker.name()
    question = factory.SubFactory(QuestionFactory)
