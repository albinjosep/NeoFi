# notes/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note, NoteHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner', 'shared_with']

class NoteHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteHistory
        fields = ['id', 'note', 'version', 'content']

