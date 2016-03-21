from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from addresses_viewer.models import Address
from addresses_viewer.api.serializers import AddressSerializer


class AddressesList(APIView):
    def get(self, request, format=None):
        snippets = Address.objects.all()
        serializer = AddressSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        Address.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

