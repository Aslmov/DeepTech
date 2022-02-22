from rest_framework import serializers
from .models import User
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('Text_chat','Text_date')


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('Theme_text','challenge_date','nbr_participants')

    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('name_module','question_text','response_text','lien')

#class pour le user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        moddel = User
        fields = ['id', 'name', 'firstName', 'pseudo', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']

