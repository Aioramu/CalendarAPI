import pytest
from authorization.models import User
from django.core import exceptions
from django.db import IntegrityError
email='test@mail.ru'
password='TEst2Pasw'
@pytest.fixture
def user_add():
    User.objects.create_user(email,password)
@pytest.mark.django_db(transaction=True)
def test_my_user(user_add):
    assert User.objects.all().count()!=0
    with pytest.raises(IntegrityError) as e_info:
        User.objects.create_user(email,password)
    assert User.objects.create_superuser(email+email,password).pk!=me.pk
