from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from modemstatus.models import ModemStatus
from modemstatus.serializers import ModemStatusSerializer

class ModemStatusViewSet(viewsets.ModelViewSet):
    queryset = ModemStatus.objects.all()
    serializer_class = ModemStatusSerializer

