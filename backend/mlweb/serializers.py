from rest_framework import serializers
from .models import Mlwebapp, CsvFiles

class MlwebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mlwebapp
        fields = ('id','title','description','completed')

class CsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvFiles
        fields = ('id', 'date_created', 'csv_file')