from datetime import datetime

from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@extend_schema(
    summary="Health Check",
    description="Returns 200 OK if the API is running",
    tags=["System"],  # Group in Swagger UI
    deprecated=False,
    responses={200: {"type": "object", "properties": {"status": {"type": "string"}}}},
    examples=[  # Example responses
        OpenApiExample("Success", value={"status": "healthy", "version": "1.0.0"})
    ],
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)


@extend_schema(
    summary="Server Time",
    description="Returns the current server time",
    responses={200: {"type": "object", "properties": {"timestamp": {"type": "string"}}}},
)
@api_view(['GET'])
@permission_classes([AllowAny])
def server_time(request):
    return Response({"timestamp": datetime.now().isoformat()}, status=status.HTTP_200_OK)
