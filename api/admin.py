from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','contact_no','profile_pic','address','availability','category')

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('id','location','lab_name','contact_info','charges','test_name','testing_at')

@admin.register(Insuarance)
class CompanyRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','company_code','contact_no','email','address')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id','seller_name','quantity','price','district','contact','profile_pic','country','price_with_transportation']

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','item_name','price','quantity','item_pic']

@admin.register(ReUpyog)
class ReUpyogAdmin(admin.ModelAdmin):
    list_display = ['id','category']

@admin.register(ReupyogArticle)
class ReupyogArticleAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','images','link']

@admin.register(Reupyogvideo)
class ReupyogvideoAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','video_link']