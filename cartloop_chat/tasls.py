# from celery.decorators import task
# from celery.utils.log import get_task_loggerfrom time import
# from .celery.inform_using_mail import send_mail_to
# sleeplogger = get_task_logger(__name__)@task(name='send_chat_notification')
# from .models import Chat, Schedule


# from celery.schedules import crontab
# CELERYBEAT_SCHEDULE = {
# 'periodic_send_email': {
#     'task': 'tasks.send_chat_notification',
#     'schedule': crontab(minute="*/60"),
# },
# }

# def send_chat_notification():
#     allChat = Chat.objects.filter(status=Chat.Status.NEW)
#     for i in allChat:
#         subject = 'Cartloop Chat'
#         message = 'Yor message has sended'
#         receiver = 'receiver_mail@gmail.com'
#         is_task_completed = False
#         error = ''
#         try:
#             is_task_completed = True
#         except Exception as err:
#             error = str(err)
#             logger.error(error)
#         if is_task_completed:
#             send_mail_to(subject, message, receivers)
#         else:
#             send_mail_to(subject, error, receivers)
#     return('first_task_done')
