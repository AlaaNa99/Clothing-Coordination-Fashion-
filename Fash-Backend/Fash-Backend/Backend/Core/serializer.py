from rest_framework.serializers import ModelSerializer
from .models import HomeModel,FirstScreenModel,SecondScreenModel,ThirdScreenModel


class HomeSerializer(ModelSerializer):
    class Meta:
        model = HomeModel
        fields = '__all__'
    
class FirstScreenSerializer(ModelSerializer):
    class Meta:
        model = FirstScreenModel
        fields = '__all__'


class SecondScreenSerializer(ModelSerializer):
    class Meta:
        model = SecondScreenModel
        fields = '__all__'


class ThirdScreenSerializer(ModelSerializer):
    class Meta:
        model = ThirdScreenModel
        fields = '__all__'


