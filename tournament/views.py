from rest_framework import viewsets, status
from rest_framework.response import Response

from api.views import CustomModelViewSet
from .serializers import TournamentSerializer
from .models import Tournament

class TournamentViewSet(CustomModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    # # ✅ GET (list)
    # def list(self, request, *args, **kwargs):
    #     try:
    #         queryset = self.get_queryset()
    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response({
    #             "success": True,
    #             "message": "Request is OK",
    #             "data": serializer.data
    #         }, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return self.handle_exception(e)

    # # ✅ GET (retrieve)
    # def retrieve(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance)
    #         return Response({
    #             "success": True,
    #             "message": "Request is OK",
    #             "data": serializer.data
    #         }, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return self.handle_exception(e)

    # # ✅ POST (create)
    # def create(self, request, *args, **kwargs):
    #     try:
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         return Response({
    #             "success": True,
    #             "message": "Tournament created successfully",
    #             "data": serializer.data
    #         }, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         return self.handle_exception(e)

    # # ✅ PUT/PATCH (update)
    # def update(self, request, *args, **kwargs):
    #     try:
    #         partial = kwargs.pop('partial', False)
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_update(serializer)
    #         return Response({
    #             "success": True,
    #             "message": "Tournament updated successfully",
    #             "data": serializer.data
    #         }, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return self.handle_exception(e)

    # # ✅ DELETE (destroy)
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #         return Response({
    #             "success": True,
    #             "message": "Tournament deleted successfully"
    #         }, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return self.handle_exception(e)
