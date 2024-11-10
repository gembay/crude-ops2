from rest_framework.decorators import api_view
from .models import Client,Products
from .serializers import ClientSerializer,ProductsSerializer
from rest_framework .response import Response
from rest_framework import status

@api_view(['GET'])
def get_client(request):
    clients = Client.objects.all()
    serializerData = ClientSerializer(clients,many=True).data
    return Response(serializerData)

@api_view(['POST'])
def create_client(request):
    data = request.data
    serializer = ClientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(['PUT','DELETE'])
def client_detail(request,pk):
    try:
        client = Client.objects.get(pk=pk)

    except Client.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if request.method == 'DELETE':
         client.delete()
         return Response(status=status.HTTP_410_GONE)
    elif request.method == 'PUT':
        data = request.data
        serializer = ClientSerializer(client,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_products(request):
    products = Products.objects.all()
    serializerData = ProductsSerializer(products,many=True).data
    return Response(serializerData)

@api_view(['POST'])
def create_products(request):
    data = request.data
    serializer = ProductsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(['PUT','DELETE'])
def products_details(request,pk):
    try:
        product = Products.objects.get(pk=pk)

    except Products.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if request.method == 'DELETE':
         product.delete()
         return Response(status=status.HTTP_410_GONE)
    elif request.method == 'PUT':
        data = request.data
        serializer = ProductsSerializer(product,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
