import logging
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MlwebSerializer,CsvSerializer
from .models import Mlwebapp, CsvFiles
import pandas as pd
import numpy as np
# Create your views here.

logger = logging.getLogger('app_api')
class Dataset:
    def __init__(self):
        self.columns = []
        self.missing ={}
        self.numerical =[]
        self.catagorical = []
        self.discrete = []
    def missingColumns(self):
        features_with_na = [features for features in self.dataset.columns if  self.dataset[features].isnull().sum()>1]
        for feature in features_with_na:
            self.missing[feature] = np.round(self.dataset[feature].isnull().mean(), 4) * 100

    def readFiles(self,df,file_name):
        self.dataset = df.copy()
        self.file_name = file_name
        self.missingColumns()
        self.columns = set(self.dataset.columns)
        self.numerical = set([feature for feature in self.dataset.columns if self.dataset[feature].dtypes != 'O'])
        self.catagorical = set([feature for feature in self.dataset.columns if self.dataset[feature].dtypes == 'O'])

    def setTarget(self,target):
        self.target = target

    def setdiscrete(self,value):
        temp = set([feature for feature in self.numerical if len(self.dataset[feature].unique()) <value])
        self.discrete = temp
        self.numerical = self.numerical - temp

@api_view(['GET', 'POST'])
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
    except CsvFiles.DoesNotExist:
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

@api_view(['GET','POST'])
def CsvDetailView(request, pk):
    if request.method == 'GET':
        # data = request.data
        # logger.info('data', data, id)
        # try:
        #     getQueryset = CsvFiles.objects.filter(id = 6)
        # except CsvFiles.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        getQueryset = CsvFiles.objects.filter(id=pk)

        serializer = CsvSerializer(getQueryset, many=True)
        
        df = pd.read_csv(str(getQueryset[0].csv_file), encoding='latin-1')
        # df = pd.read_csv(csv_file)
        current_dataset = Dataset()
        file_name = str(getQueryset[0].csv_file)
        current_dataset.readFiles(df,file_name)
        # pickled_object = pickle.dumps(current_dataset)
        # r.set('current_dataset', pickled_object )
        # r.set('file_name',file_name)
        features = list(df.columns)
        #features dataset
        #graphs dataset
        # logger.info('data 2', dataset.head(5))
        summary = df[features]
        summary = summary.describe()
        df_dict = {
            "head": df.head(5).to_html(index=False, justify='justify-all'),
            "features": features,
            "summary": summary.to_html(justify='justify-all')
        }
        return Response(df_dict)


    
 