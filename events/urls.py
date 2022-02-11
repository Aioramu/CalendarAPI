from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.EventsView.as_view()),
]
