from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from .models import Events
from .serializers import EventSerializer
from rest_framework import generics
from rest_framework.response import Response


class EventsView(generics.GenericAPIView):
    queryset = Events.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    def post(self,request):
        data=request.data.copy()
        data['user']=request.user.email
        serializer=self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    def get(self,request):
        queryset=self.get_queryset().filter(user=request.user.email).order_by('time_from')
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)
