from rest_framework import serializers
from .models import *


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Poll
        fields = '__all__'

    def validate(self, attrs):
        if attrs['start_date'] >= attrs['end_date']:
            raise serializers.ValidationError("تاریخ شروع باید قبل از تاریخ پایان باشد")
        return attrs
