from rest_framework.serializers import ModelSerializer
from cloro.models import CloroModel

class CloroSerializer(ModelSerializer):
    class Meta:
        model = CloroModel
        fields = '__all__'