from .models import Events
from .serializers import EventSerializer
from rest_framework import exceptions
import datetime
import pytz

class OuterFormatter:

    def __init__(self,request,queryset=Events.objects.all(),serializer=EventSerializer):
        self.queryset=queryset
        self.request=request
        self.serializer=serializer

    @property
    def _queryset(self):
        return self._ordertime()

    def _ordertime(self):
        params=self.request.query_params
        if 'day' in params and params['day']!=None:
            try:
                day=datetime.datetime.fromisoformat(params['day'])
                return self.queryset.filter(time_from__date=params['day'])
            except:

                raise exceptions.ValidationError("wrong dateformat in day params")
        elif 'month' in params:
            try:
                date=datetime.datetime.fromisoformat(params['month'])
                month=date.month
                year=date.year
                return self.queryset.filter(time_from__month=month,time_from__year=year)
            except:
                raise exceptions.ValidationError("wrong dateformat in month params")
        else:
            raise exceptions.ValidationError("you need to declare what day need to agregate")
    def group_by_date(self):
        queryset=self._queryset
        print(queryset)
        dates={}
        for i in queryset:
            data=i.time_from+datetime.timedelta(hours=3)
            if str(data.date()) not in dates.keys():
                dates[str(data.date())]=[]
            serializer=self.serializer(i)
            dates[str(data.date())].append(serializer.data)
        return dates
