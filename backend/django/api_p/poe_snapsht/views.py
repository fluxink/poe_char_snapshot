from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SnapShots, Characters, Accounts
from .serializers import CharSerializer, SnapShotSerializer


class SnapShotsList(APIView):

    def get(self, request, character, format=None, **kwargs):
        char = Characters.objects.get(character=character)

        snapshots = SnapShots.objects.filter(character_id=char)
        serializer = SnapShotSerializer(snapshots, many=True)

        return Response(serializer.data)


class CharList(APIView):

    def get(self, request, account_name, format=None):
        account = Accounts.objects.get(account_name=account_name)

        chars = Characters.objects.filter(account_id=account)
        serializer = CharSerializer(chars, many=True)

        return Response(serializer.data)