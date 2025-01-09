from api.models import ChatMessage, Profile, User
from django.db.models import Subquery, OuterRef, Q
from django.db import connection
from pprint import pprint

def run():
        user_id = 1
        messages = ChatMessage.objects.filter(Q(receiver=user_id) | Q(sender=user_id))
        print(messages)
       
        # print(ChatMessage.objects.all())