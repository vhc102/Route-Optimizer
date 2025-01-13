from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .serializers import RouteRequestSerializer


class FuelRouteView(APIView):

    @swagger_auto_schema(request_body=RouteRequestSerializer)
    def post(self, request):
        serializer = RouteRequestSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # Delegate to the serializer to calculate all details
                details = serializer.calculate_details()
                return Response(details, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)