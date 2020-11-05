from rest_framework_json_api import serializers
from cartloop_chat.models import Chat, Client, Conversation, Operator, Schedule


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        exclude = ['client', 'conversation']


class ConversationSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ('chat', 'client_id','id', 'operator_id','operatorGroup')


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = ('__all__')
