from django.shortcuts import render
from creditor.models import Creditor
from rest_framework import viewsets
from creditor.serializers import *

class CreditorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
