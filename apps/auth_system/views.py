from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import User
from apps.permissions_system.models import Role

from .services import (
    hash_password,
    check_password,
    create_token
)


class RegisterView(APIView):

    def post(self, request):

        data = request.data

        if data['password'] != data['repeat_password']:
            return Response(
                {'error': 'Passwords do not match'},
                status=400
            )

        role = Role.objects.filter(name='user').first()

        if not role:
            role = Role.objects.create(name='user')

        user = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            middle_name=data.get('middle_name', ''),
            email=data['email'],
            password=hash_password(data['password']),
            role=role
        )

        return Response({
            'message': 'User created',
            'user_id': user.id
        })


class LoginView(APIView):

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(
            email=email,
            is_active=True
        ).first()

        if not user:
            return Response(
                {'error': 'User not found'},
                status=404
            )

        if not check_password(password, user.password):
            return Response(
                {'error': 'Invalid password'},
                status=400
            )

        token = create_token(user.id)

        return Response({
            'token': token
        })