from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:  # search for the concept of Meta()
        model = Student
        fields = '__all__'

