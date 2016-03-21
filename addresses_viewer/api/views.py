from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from addresses_viewer.models import Address
from addresses_viewer.api.serializers import AddressSerializer


@api_view(['GET', 'POST'])
def addresses_list(request):
    if request.method == 'GET':
        snippets = Address.objects.all()
        serializer = AddressSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def clear_data(request):
    Address.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)        

