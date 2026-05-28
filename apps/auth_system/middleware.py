from apps.users.models import User
from .services import decode_token


class AuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.user = None

        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                token = auth_header.split(' ')[1]

                payload = decode_token(token)

                user = User.objects.get(
                    id=payload['user_id'],
                    is_active=True
                )

                request.user = user

            except Exception:
                request.user = None

        response = self.get_response(request)

        return response