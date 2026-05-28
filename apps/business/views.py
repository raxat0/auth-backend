from rest_framework.views import APIView
from rest_framework.response import Response

from apps.permissions_system.models import (
    BusinessElement,
    AccessRule
)

from apps.permissions_system.services import has_permission


class ProductsView(APIView):

    def get(self, request):

        if not request.user:
            return Response(
                {'error': 'Unauthorized'},
                status=401
            )

        element = BusinessElement.objects.filter(
            name='products'
        ).first()

        if not element:
            element = BusinessElement.objects.create(
                name='products'
            )

            AccessRule.objects.create(
                role=request.user.role,
                element=element,
                read_permission=True
            )

        allowed = has_permission(
            request.user,
            'products',
            'read'
        )

        if not allowed:
            return Response(
                {'error': 'Forbidden'},
                status=403
            )

        return Response([
            {
                'id': 1,
                'name': 'Phone'
            },
            {
                'id': 2,
                'name': 'Laptop'
            }
        ])