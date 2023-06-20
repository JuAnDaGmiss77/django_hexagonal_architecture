from users.application.services.user_service import UserService
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

class UserController:
    
    @api_view(['POST'])
    @parser_classes([JSONParser])
    def create_user(request):
        print(request.data)

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        user_service = UserService()
        user_service.create_user(username, password, email)

        return Response({'message': 'created'}, status=201)
