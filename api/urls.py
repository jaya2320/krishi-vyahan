from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('get_lab_details/',views.LabDetails.as_view()),
    path('get_insuarance_details/',views.InsuaranceDetails.as_view()),
    path('get_transport_details/',views.TransportDetails.as_view()),
    path('crop_analysis/',views.CropAnalysis.as_view()),
    path("crop_season/",views.CropSeasonPrediction.as_view()),
    path('get_seller_details/',views.SellerView.as_view()),
    path('get_shop_details/',views.ShopView.as_view()),
    path('get_nutrition_list/',views.NutritionView.as_view(),name="get_nutrition_list")
]