from rest_framework import serializers

class SymptomInputSerializer(serializers.Serializer):
    symptom = serializers.CharField()
    language = serializers.CharField(required=False, default='en')
    
    