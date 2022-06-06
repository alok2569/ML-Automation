import logging
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MlwebSerializer,CsvSerializer
from .models import Mlwebapp, CsvFiles
# Create your views here.

logger = logging.getLogger('app_api')

@api_view(['GET'])
def MlwebView(request):
    try:
        mlwebRes = Mlwebapp.objects.all()
    except Mlwebapp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MlwebSerializer(mlwebRes, many=True)
        # logging.debug('abcd')
        return Response(serializer.data)
# class MlwebView(viewsets.ModelViewSet):
#     serializer_class = MlwebSerializer
#     queryset = Mlwebapp.objects.all()

@api_view(['GET', 'POST'])
def CsvView(request):
    try:
        getQueryset = CsvFiles.objects.all()
    except Mlwebapp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # getQueryset = CsvFiles.objects.all()
        serializer = CsvSerializer(getQueryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        logger.info(request.data)
        serializer = CsvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)
    
 