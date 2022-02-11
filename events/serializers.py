from rest_framework import serializers
from .models import Events,Holidays
from rest_framework.validators import UniqueTogetherValidator
import datetime

class EventSerializer(serializers.ModelSerializer):

    time_to=serializers.DateTimeField(allow_null=True,default=None)
    class Meta:
        model = Events
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Events.objects.all(),
                fields=['user', 'time_from','time_to']
            ),
            UniqueTogetherValidator(
                queryset=Events.objects.all(),
                fields=['time_from','time_to']
            ),
            UniqueTogetherValidator(
                queryset=Events.objects.all(),
                fields=['user','time_to']
            ),
            UniqueTogetherValidator(
                queryset=Events.objects.all(),
                fields=['user','time_from']
            ),
        ]
    def validate(self,data):
        if data['time_to']==None:
            data['time_to']=data['time_from']
            data['time_to']=data['time_to'].replace(hour=23,minute=59)
            print(data['time_to'])
        if data['time_to']<data['time_from']:
            raise serializers.ValidationError("time_to must be later than time_from ")
        count=len(Events.objects.filter(
        time_from__range=[data['time_from'],data['time_to']],
        user=data['user']))
        if count>0:
            raise serializers.ValidationError({"time_from": "For this time,you already have event "})
        count=len(Events.objects.filter(
        time_to__range=[data['time_from'],data['time_to']],
        user=data['user']))
        if count>0:
            raise serializers.ValidationError({"time_to": "For this time,you already have event "})
        return data
