import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .models import SnapShots, Characters, Accounts
from .serializers import CharSerializer, SnapShotSerializer
from .permissions import IsOwnerOrCreateOnly
from .modules import parse
from .management.commands import fetchchars


class SnapShotsList(APIView):

    def get(self, request, character, format=None, **kwargs):
        char = Characters.objects.get(character=character)

        snapshots = SnapShots.objects.filter(character_id=char)
        serializer = SnapShotSerializer(snapshots, many=True)

        return Response(serializer.data)

class GetCharsNames(APIView):

    def post(self, request, *args, **kwargs):
        account_name = request.data.get('account_name')
        characters = parse.get_character_list(account_name)
        characters_names = []
        for char in characters:
            lvl = char.get('level')
            name = char.get('name')
            char_class = char.get('class')
            league = char.get('league')
            characters_names.append({
                'level': lvl,
                'name': name,
                'class': char_class,
                'league': league
            })
        json_chars = json.dumps(characters_names)
        return Response(json_chars)


class CharList(APIView):

    def get(self, request, account_name, format=None):
        account = Accounts.objects.get(account_name=account_name)

        chars = Characters.objects.filter(account_id=account)
        serializer = CharSerializer(chars, many=True)

        return Response(serializer.data)


class CharCrtUpdDel(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharSerializer
    # permission_classes = (permissions.IsAuthenticated,
    #                     IsOwnerOrCreateOnly)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    # def get_queryset(self):
    #     return Characters.objects.get(character=self.request.POST.get('character'))

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(character=self.request.POST.get('character'))
        self.check_object_permissions(self.request, obj)
        return obj

class CreateSnapshots(APIView):

    def get(self, request):
        t = fetchchars.Command()
        t.handle()
        return Response('Started')
