from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class CustomModelViewSet(viewsets.ModelViewSet):
    """
    সব ViewSet এর জন্য base class, যা automatic custom JSON response দিবে।
    """
    def handle_exception(self, exc):
        """
        DRF এর default exception handle করা method override করছি।
        সব exception কে custom response এ রূপান্তর করবে।
        """
        # যদি এটি already DRF APIException হয়, status_code নেবে
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
