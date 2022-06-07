from rest_framework import serializers
from .models import StudentsInfo

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentsInfo
        fields = '__all__'