from First_bot.models import Product,ProductDescription
from rest_framework import serializers
#from myapp.serializers import ArticleSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','link','name']



class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDescription
        fields = '__all__'


