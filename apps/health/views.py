from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Health Check",
    description="Returns 200 OK if the API is running",
    responses={200: {"type": "object", "properties": {"status": {"type": "string"}}}}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response(
        {"status": "healthy"},
        status=status.HTTP_200_OK
    ) 