from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from rest_framework import serializers, status
from .serializers import *
import pickle
import joblib
import json
import pandas as pd


# Create your views here.
class LabDetails(APIView):
    serializer_class = LabSerializer
    def get(self,request):
        try:
            labs = Lab.objects.all()
            lab_data = LabSerializer(labs,many=True)
            return Response({'lab':lab_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TransportDetails(APIView):
    serializer_class = TransportSerializer
    def get(self,request):
        try:
            transports = Transport.objects.all()
            transport_data = TransportSerializer(transports,many=True)
            return Response({'transport':transport_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InsuaranceDetails(APIView):
    serializer_class = InsuaranceSerializer
    def get(self,request):
        try:
            insuarances = Insuarance.objects.all()
            insuarance_data = InsuaranceSerializer(insuarances,many=True)
            return Response({'insurance':insuarance_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)





class CropAnalysis(APIView):
    serializer_class = CropAnalysisSerializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
             
                n= serializer.validated_data.get("nitrogen")
                p=serializer.validated_data.get("phosphorus")
                k=serializer.validated_data.get("potassium")
                temp=serializer.validated_data.get("temperature")
                
                humidity=serializer.validated_data.get("humidity")
                ph=serializer.validated_data.get("ph")
                rainfall=serializer.validated_data.get("rainfall")

                mj=joblib.load('crop_analysis_prediction')

                temp=[n,p,k,temp,humidity,ph,rainfall]

                
                
                predi=mj.predict([temp])
               
                return Response({'predict':predi}, status=status.HTTP_200_OK)
        else:
                
                return Response({"status": "failed", "message": "in else"}, status=status.HTTP_400_BAD_REQUEST)
        

summercrops = ['paddy','maize','brinjal','tomato','watermelon','bitter gourd','onion','pigeonpeas', 'mothbeans', 'blackgram', 'mango', 'grapes' ,'orange', 'papaya']
wintercrops = ['maize' ,'pigeonpeas' ,'lentil', 'pomegranate', 'grapes', 'orange','barley,','gram','mustard','oat','grapes','guava','lemon','radish']
rainycrops = ['rice', 'papaya', 'coconut','cucumber','tomato','radish','beans','green chilies','okra','brinjal','cotton','sugarcane','tea']
data = pd.read_csv("Crop_recommendation.csv")
list_of_label = (data['label'].unique())
class NutritionView(APIView):
    serializer_class = NutritionSerializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
             
                crop_name = serializer.validated_data.get("crop_name")
                if crop_name in list_of_label:
                    result = (data[data['label']==crop_name].head()).to_json(orient="records")
                elif crop_name in summercrops:
                    result = (data[data['label']=="maize"].head()).to_json(orient="records")
                elif crop_name in wintercrops:
                    result = (data[data['label']=="grapes"].head()).to_json(orient="records")
                elif crop_name in rainycrops:
                    result = (data[data['label']=="coconut"].head()).to_json(orient="records")
                else:
                    result = (data[data['label']=="maize"].head()).to_json(orient="records")

                return JsonResponse(json.loads(result), safe = False)
        else:
            return Response({"status":"failed"})



class CropSeasonPrediction(APIView):
    serializer_class = CropSeasonPredictionSerializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
             
                n= serializer.validated_data.get("nitrogen")
                p=serializer.validated_data.get("phosphorus")
                k=serializer.validated_data.get("potassium")
                temp=serializer.validated_data.get("temperature")
                
                humidity=serializer.validated_data.get("humidity")
                ph=serializer.validated_data.get("ph")
                rainfall=serializer.validated_data.get("rainfall")

                mj=joblib.load('crop_season_prediction')

                temp=[n,p,k,temp,humidity,ph,rainfall]

           
                
                predi=mj.predict([temp])
                if predi in summercrops:
                    ans = summercrops
                elif predi in wintercrops:
                    ans = wintercrops
                else:
                    ans = rainycrops
               
                return Response({'predict':ans}, status=status.HTTP_200_OK)
        else:
                
                return Response({"status": "failed", "message": "in else"}, status=status.HTTP_400_BAD_REQUEST)

class SellerView(APIView):
    serializer_class = SellerSerializer
    def get(self,request):
        try:
            sellers = Seller.objects.all()
            seller_data = SellerSerializer(sellers,many=True, context={'request':request})
            return Response({'seller':seller_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ShopView(APIView):
    serializer_class = ShopSerializer
    def get(self,request):
        try:
            shops = Shop.objects.all()
            shop_data = ShopSerializer(shops,many=True)
            return Response({'shop':shop_data.data})
        except Exception as e:
            print(e)
            return Response({'status': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request,'index.html')

