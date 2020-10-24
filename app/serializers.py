from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        exclude = ['terms']

    def get_user(self, obj):
        return obj.user.username


class AgreeTermsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['terms', 'user']

    def get_user(self, obj):
        return obj.user.username


class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qualification
        fields = ['title', 'icon']


class QualificationCreateSerializer(serializers.ModelSerializer):

    # qualification = QualificationSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['qualification', 'user', 'is_qualified']


