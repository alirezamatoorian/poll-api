from rest_framework import serializers
from .models import *
from django.utils import timezone


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['text', 'poll']
        read_only_fields = ['poll']


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ['creator']

    def validate(self, attrs):
        start_date = attrs['start_date']
        end_date = attrs['end_date']
        if start_date >= end_date:
            raise serializers.ValidationError("تاریخ شروع باید قبل از تاریخ پایان باشد")
        if start_date < timezone.now():
            raise serializers.ValidationError("تاریخ شروع باید بعد از زمان فعلی باشد")
        return attrs

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        poll = Poll.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(poll=poll, **choice_data)

        return poll
