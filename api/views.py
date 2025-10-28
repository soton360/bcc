from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class CustomModelViewSet(viewsets.ModelViewSet):
    
    def handle_exception(self, exc):
        if isinstance(exc, APIException):
            status_code = exc.status_code
            detail = exc.detail
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            detail = str(exc)

        return Response({
            "success": False,
            "message": detail
        }, status=status_code)
