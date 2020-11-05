from rest_framework.urlpatterns import format_suffix_patterns
from cartloop_chat.views import ConversationViewSet, ChatViewSet
from django.urls import path

conversationUrls = ConversationViewSet.as_view({
    'get': 'retrieve'
})
chatUrls = ChatViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# sc = ScheduleViewSet.as_view({
#     'get': 'list',
# })


urlpatterns = format_suffix_patterns([
    path('conversation/<int:pk>/', conversationUrls, name='conversation-detail'),
    path('chat/', chatUrls, name='chat')
    # path('sc/', sc)
])
