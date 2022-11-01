from urlshortner.models import Url
from .serializers import UrlSerializer, UrlDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'PUT', 'DELETE'])
def url_detail(request, pk):
    try:
        url = get_object_or_404(Url, pk=pk)
    except Url.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UrlDetailSerializer(url)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UrlSerializer(url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def url_list(request):
    if request.method == 'GET':
        url = Url.objects.all()
        serializer = UrlSerializer(url, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

