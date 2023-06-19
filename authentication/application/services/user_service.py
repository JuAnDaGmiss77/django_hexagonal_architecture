from django.contrib.auth.models import User
import re

class UserService:
    def _validate_user(self, username:str, password:str, email:str):
        if not username:
            raise ValueError('username is required')
        
        if not password:
            raise ValueError('password is required')
        
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError('Invalid email format')
        
    def create_user(self, username:str, password:str, email:str):
        self._validate_user(username, password, email)

        User.objects.create_user(username=username, password=password, email=email)

