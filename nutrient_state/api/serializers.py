from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from nutrient_state.models import LettuceNutrients

class LettuceNutrientsSerializer(ModelSerializer):
    class Meta:
        model = LettuceNutrients
        fields = ['id', 'created_at', 'ph_value', 'tds_value', 'tank_level']
