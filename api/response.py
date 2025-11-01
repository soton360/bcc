from rest_framework.response import Response

# def success_response(data=None, message="Request successful", status_code=200):
#     """
#     Returns a consistent success response for all APIs.
#     """
#     return Response({
#         "success": True,
#         "message": message,
#         "data": data
#     }, status=status_code)

def error_response(message="An error occurred", status_code=400):
    """
    Returns a consistent error response for all APIs.
    """
    return Response({
        "message": message
    }, status=status_code)

