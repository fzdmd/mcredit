from rest_framework import serializers
from borrower.models import Borrower


class BorrowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Borrower
        fields = ('__all__')
