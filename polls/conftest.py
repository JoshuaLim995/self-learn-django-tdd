import pytest
from polls.factories import QuestionFactory, ChoiceFactory

from pytest_factoryboy import register

# register your factories here
register(QuestionFactory)
register(ChoiceFactory)
