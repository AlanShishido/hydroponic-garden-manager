from rest_framework.viewsets import ModelViewSet
from nutrient_state.models import LettuceNutrients
from .serializers import LettuceNutrientsSerializer


class LettuceNutrientsViewSet(ModelViewSet):

    queryset = LettuceNutrients.objects.all()
    serializer_class = LettuceNutrientsSerializer
