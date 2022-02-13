import pytest
from authorization.models import User
from events.models import Events
from events.serializers import EventSerializer
from authorization.tests.registration_tests import user_add
from datetime import datetime,timedelta
now=datetime.now()
@pytest.mark.django_db(transaction=True)
@pytest.fixture
def event_create():
    data={
        "summary": "test",
        "time_from": now+timedelta(hours=5),#почему то при фикстуре таймзона не подтягивается
        "time_to": now+timedelta(hours=6),
        "notification": "За час",
        "user":User.objects.last()
        }
    Events.objects.create(**data)

@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize('time_from,time_to,notification,result',
[(now+timedelta(hours=2),now+timedelta(hours=2),"За час",False),
(now+timedelta(hours=3),now+timedelta(hours=3),"За час",False),
(now+timedelta(hours=4),now+timedelta(hours=4,minutes=1),"За час",True),
(now+timedelta(hours=4),now+timedelta(hours=3,minutes=1),"За час",False),
(now+timedelta(hours=4),now+timedelta(hours=4,minutes=1),"1",False),
(now+timedelta(hours=4),now+timedelta(hours=3,minutes=1),"За час",False),
])
def test_create_events_serializer(user_add,event_create,time_from,time_to,notification,result):
    data={
        "summary": "testcase",
        "time_from":time_from,
        "time_to":time_to,
        "notification": notification,
        "user":User.objects.last()
    }

    serializer=EventSerializer(data=data)
    assert serializer.is_valid()==result
