
from rest_framework import serializers
from django.contrib.auth.models import User
from note.models import Note



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializerfields = [
            "id",
            "username",
            "email"
        ]

class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "body",
            "user",
            "slug",
        ]