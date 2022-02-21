from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
def index_view(request):
    return HttpResponse("Tout est ok")

class Challengeview(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()

class Moduleview(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class Messageview(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()