from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.


class Client(models.Model):
    username = models.TextField(max_length=100)


class Operator(models.Model):
    name = models.TextField(max_length=100)

class Conversation(models.Model):
    class OperatorGroup(models.TextChoices):
        SALE = 'sales'
        SUPPORT = 'support'
        TECHNICAL = 'technical'
    operatorGroup = models.CharField(
        max_length=10, choices=OperatorGroup.choices, default=OperatorGroup.SALE)
    storeId = models.IntegerField()
    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, db_column='operatorId', related_name='operatorId')
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, db_column='clientId', related_name='clientId')


class Chat(models.Model):
    class Status(models.TextChoices):
        SENT = 'sent'
        NEW = 'new'
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.NEW)
    payload = models.TextField(max_length=300)
    utc_date = models.DateTimeField(
        db_column='utc-date', default=datetime.datetime.now(datetime.timezone.utc))
    client = models.ForeignKey(Client, models.CASCADE, db_column='userId')
    conversation = models.ForeignKey(
        Conversation, models.CASCADE, related_name="chat")


class Schedule(models.Model):
    class NotificationType(models.TextChoices):
        EMAIL = 'email'
        SMS = 'SMS'
    notificationtype = models.CharField(max_length=10, choices=NotificationType.choices, default=NotificationType.EMAIL)
    created_at = models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc))
    Chat = models.ForeignKey(Chat,models.CASCADE)
    isSuccess = models.BooleanField(default=False)