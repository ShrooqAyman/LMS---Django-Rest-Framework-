from issues.models import Issue
from rest_framework import serializers

class UserIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'



