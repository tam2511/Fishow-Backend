from rest_framework import serializers
from other_models.models import Statistics_main_page


class Statistics_main_pageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics_main_page
        fields = '__all__'
