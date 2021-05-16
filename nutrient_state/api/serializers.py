from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from nutrient_state.models import LettuceNutrients

class LettuceNutrientsSerializer(ModelSerializer):
    class Meta:
        model = LettuceNutrients
        fields = ['id', 'created_at', 'status_code']
