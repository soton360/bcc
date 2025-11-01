from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from .response import error_response

def custom_exception_handler(exc, context):
    """
    Global exception handler for all API errors.
    Converts DRF ValidationError or dict-like errors into simple messages.
    """

    response = exception_handler(exc, context)

    if response is not None:
        detail = response.data

        # Flatten nested error messages
        if isinstance(detail, dict):
            messages = []
            for field, errors in detail.items():
                if isinstance(errors, (list, tuple)):
                    messages.extend(errors)
                else:
                    messages.append(str(errors))
            message = messages[0] if messages else str(detail)
        elif isinstance(detail, list):
            message = detail[0] if detail else "An error occurred."
        else:
            message = str(detail)
        return error_response(message=message, status_code=response.status_code)
        

    # Unhandled exception (server errors)
    return error_response(message=str(exc), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    