from .models import Issue
from rest_framework import serializers

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'



