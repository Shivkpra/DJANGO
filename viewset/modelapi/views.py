from rest_framework import viewsets
from django.shortcuts import render
from .models import Cutomer
from.serializer import CutomerSerializer

# Create your views here.


class CutomerModelViewSet(viewsets.ModelViewSet):

    queryset = Cutomer.objects.all()
    serializer_class = CutomerSerializer


class ReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Cutomer.objects.all()
    serializer_class = CutomerSerializer
