from django.db.models import Count
from rest_framework import generics
from rest_framework.serializers import ValidationError

from .models import *
from .serializers import *


class HomeView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        profile = serializer.save()
        profile.user = self.request.user
        profile.save()


class TermsCreateView(generics.ListCreateAPIView):
    serializer_class = AgreeTermsSerializer

    def get_queryset(self):
        qs = UserProfile.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        terms_count = Terms.objects.aggregate(Count('title'))
        posted_terms_count = self.request.POST.getlist('terms')
        if terms_count['title__count'] != len(posted_terms_count):
            raise ValidationError('Нужно выбрать все поля.')
        terms_creation = serializer.save()
        terms_creation.user = self.request.user
        terms_creation.save()


class QualificationView(generics.ListCreateAPIView):
    serializer_class = QualificationCreateSerializer

    def get_queryset(self):
        qs = UserProfile.objects.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        qual_data = serializer.save()
        qual_data.user = self.request.user
        qual_data.save()

        print(qual_data.id)
