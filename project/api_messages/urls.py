from . import api

from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("message/", api.MessageView.as_view()),
    path("message/<vk_id>", api.MessageView.as_view())
]
