# serializers.py
from rest_framework import serializers
from master.models import NationMaster, StateMaster, CityMaster


class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationMaster
        fields = ['id', 'name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMaster
        fields = ['id', 'name', 'nation']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityMaster
        fields = ['id', 'name', 'state']
