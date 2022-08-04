from rest_framework import serializers
from .models import SnapShots, Characters, Accounts


class AccountSerializer(serializers.Serializer):
    account_name = serializers.CharField()

class SnapShotSerializer(serializers.Serializer):
    character_info = serializers.JSONField()
    items = serializers.JSONField()
    passives =  serializers.JSONField()
    time = serializers.DateTimeField()

class CharSerializer(serializers.Serializer):
    account = AccountSerializer()
    character = serializers.CharField()
    league = serializers.CharField()
    tracked = serializers.BooleanField()

    def create(self, validated_data):
        account = Accounts.objects.get_or_create(account_name=validated_data.get('account')['account_name'])
        validated_data.pop('account')
        return Characters.objects.get_or_create(account=account[0], **validated_data)[0]

    def update(self, instance, validated_data):
        instance.tracked = validated_data.get('tracked', instance.tracked)
        instance.save()
        return instance