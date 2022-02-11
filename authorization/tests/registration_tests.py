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
    
@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize('email,password,password2,result',
[('test@mailru','TEst2Pasw','TEst2Pasw',False),
('test@mail.ru','TEst2Pasw','TEst2Pasww',False),
('testss@mail.ru','TEst2Pasw','TEst2Pasw',True),
('test@mail.ru','228test','228test',False)
])
def test_registration_serializer(user_add,email,password,password2,result):
    data={
    "email":email,
    "password":password,
    "password2":password2
    }
    from authorization.serializers import RegistrationSerializer
    serializer = RegistrationSerializer(data=data)
    assert serializer.is_valid()==result
