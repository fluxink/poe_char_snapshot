from rest_framework import serializers
from .models import SnapShots, Characters, Accounts
from poe_snapsht.modules import parse
import asyncio


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

        obj, created = Characters.objects.get_or_create(account=account[0], **validated_data)
        if created:
            chars = asyncio.run(parse.start_fetch(((account[0].account_name, obj.character),)))
            for char in chars:
                SnapShots.objects.create(character=obj,
                    character_info=char[1],
                    items=char[2],
                    passives=char[3],
                    xml_code=char[4]
                )
        return obj

    def update(self, instance, validated_data):
        instance.tracked = validated_data.get('tracked', instance.tracked)
        instance.save()
        return instance