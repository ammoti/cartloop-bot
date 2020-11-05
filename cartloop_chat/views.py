from django.shortcuts import render
from .models import Chat, Client, Conversation, Schedule
from .serializers import ChatSerializer, ClientSerializer, ConversationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
import datetime
import re
import json


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ConversationSerializer(user)
        return Response(serializer.data)
    http_method_names = ['get']


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def list(self, request):
        queryset = Chat.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, validated_data):
        try:
            conversationId = validated_data.data['conversationId']
            payload, userId = validated_data.data['chat']['payload'], validated_data.data['chat']['userId']
            if(not payloadValid(payload)):
                error = {'code': 404, 'result': 'Payload has invalid char'}
                return Response(json.dumps(error))
            client = get_object_or_404(Client, pk=userId)
            conversation = get_object_or_404(Conversation, pk=conversationId)
            newChat = Chat.objects.create(client=client, status=Chat.Status.NEW, payload=payload, utc_date=datetime.datetime.now(
                datetime.timezone.utc), conversation=conversation)
            newChat.save()
            result = {'code': 200, 'result': newChat.id}
            if(newChat.id > 0):
                newSchedule = Schedule.objects.create(notificationtype=Schedule.NotificationType.EMAIL,created_at=datetime.datetime.now(
                datetime.timezone.utc),Chat=newChat)
                newSchedule.save()
            return Response(json.dumps(result))
        except Exception as e:
            error = {'code': 500, 'result': e}
            return Response(json.dumps(error))

    http_method_names = ['get', 'post']

# class ScheduleViewSet(viewsets.ModelViewSet):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer

def payloadValid(str):
    re2 = re.compile(
        r'[?@~^%&\*\{\}.!#\\$/\(\)\-\w\s+]*')
    if re2.fullmatch(str):
        return True
    else:
        return False
