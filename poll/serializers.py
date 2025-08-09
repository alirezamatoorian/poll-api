from rest_framework import serializers
from .models import *


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        mode = Poll
        fields = '__all__'

    def validate(self, attrs):
        if attrs['start_date'] >= attrs['end_date']:
            raise serializers.ValidationError("تاریخ شروع باید قبل از تاریخ پایان باشد")
        return attrs
