from django.urls import path
from users.infrastructure.rest_api.controllers.user_controller import UserController

urlpatterns = [
    path('create_user/', UserController.create_user),
]
