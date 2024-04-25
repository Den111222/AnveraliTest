from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', views.WebhookView.as_view(), name='webhook'),
]
