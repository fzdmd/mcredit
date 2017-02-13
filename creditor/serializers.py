from rest_framework import serializers
from creditor.models import Creditor


class CreditorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creditor
        fields = ('__all__')
