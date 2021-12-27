from . models import *
from rest_framework import serializers, status

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields= '__all__'

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields= '__all__'

class InsuaranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insuarance
        fields= '__all__'

class CropAnalysisSerializer(serializers.Serializer):
    nitrogen = serializers.IntegerField()
    phosphorus = serializers.IntegerField()
    potassium = serializers.IntegerField()
    temperature = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    humidity = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    ph = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    rainfall = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places

class CropSeasonPredictionSerializer(serializers.Serializer):
    nitrogen = serializers.IntegerField()
    phosphorus = serializers.IntegerField()
    potassium = serializers.IntegerField()
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    ph = serializers.FloatField()
    rainfall = serializers.FloatField()

    '''
    temperature = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    humidity = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    ph = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    rainfall = serializers.DecimalField(max_digits=10,decimal_places=5)#should be round to 2 decimal places
    '''


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields= '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields= '__all__'