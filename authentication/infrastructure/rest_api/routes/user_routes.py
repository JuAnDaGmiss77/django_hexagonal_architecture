from django.urls import path
from authentication.infrastructure.rest_api.controllers.user_controller import UserController

urlpatterns = [
    path('create_user/', UserController.create_user),
]
