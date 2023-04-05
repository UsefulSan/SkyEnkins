from rest_framework import serializers

from app.models import User, File


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file', 'mark', 'created', 'changed']
