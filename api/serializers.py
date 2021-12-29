from . models import *
from rest_framework import serializers, status

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields= '__all__'

class TransportSerializer(serializers.ModelSerializer):
    def get_profile_image(self,obj):
        try:
            request = self.context.get('request')
            return 'https://krishi-vyahan.herokuapp.com' + obj.profile_pic.url
        except:
            return None
    profile_image = serializers.SerializerMethodField()
    class Meta:
        model = Transport
        fields= [
            'company_name',
            'contact_no',
            'profile_image',
            'address' ,
            'availability' ,
            'category',
        ]

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
    def get_profile_image(self,obj):
        try:
            request = self.context.get('request')
            
            return 'https://krishi-vyahan.herokuapp.com' + obj.profile_pic.url
        except:
            return None
    profile_image = serializers.SerializerMethodField()
    class Meta:
        model = Seller
        fields= [
                'seller_name',
                'item_name',
                'quantity' ,
                'price',
                'district' ,
                'state',
                'country',
                'contact' ,
                'profile_image',
                'price_with_transportation'
        ]


class ShopSerializer(serializers.ModelSerializer):
    def get_item_image(self,obj):
        try:
            request = self.context.get('request')
            return 'https://krishi-vyahan.herokuapp.com' + obj.item_pic.url
        except:
            return None
    item_image = serializers.SerializerMethodField()
    class Meta:
        model = Shop
        fields= [
                'item_name',
                'price',
                'quantity',
                'item_image',
        ]