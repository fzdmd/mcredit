from django.shortcuts import render
from borrower.models import Borrower
from rest_framework import viewsets
from borrower.serializers import *

class BorrowerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
