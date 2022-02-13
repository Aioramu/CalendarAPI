from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from .models import Events
from .serializers import EventSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
import datetime

from .tasks import mail_sender
from .formatters import OuterFormatter


class EventsView(generics.GenericAPIView):
    queryset = Events.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    def post(self,request):
        data=request.data.copy()
        data['user']=request.user.email
        serializer=self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            event=serializer.save()
            start_time=event.time_from-datetime.timedelta(hours=event.get_notification_display())
            print(start_time)
            mail_sender.apply_async(args=[event.id], eta=start_time)
            return Response(serializer.data)
    def get(self,request):
        queryset=self.get_queryset().filter(user=request.user.email).order_by('time_from')
        b=OuterFormatter(queryset=queryset,request=request)
        data=b.group_by_date()

        return Response(data)
