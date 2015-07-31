from rest_framework import serializers
from modemstatus.models import ModemStatus

class ModemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModemStatus
        fields = ('status_data', 'weather_data',)

