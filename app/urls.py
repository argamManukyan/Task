from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('terms/', TermsCreateView.as_view(),name='terms_create'),
    path('qualification/', QualificationView.as_view(),name='qualification')

]
