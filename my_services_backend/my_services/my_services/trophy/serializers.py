from rest_framework.serializers import ModelSerializer

from my_services.users.serializers import SimpleUserSerializer
from .models import Trophy


class TrophySerializer(ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = Trophy
        fields = [
            "id",
            "user",
            "text",
            "description",
            "date_created",
            "image"
        ]
