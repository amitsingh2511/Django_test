# app_name/serializers.py
from rest_framework import serializers
from .models import Application, Compliance

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class ComplianceSerializer(serializers.ModelSerializer):
    applications = ApplicationSerializer(many=True)

    class Meta:
        model = Compliance
        fields = '__all__'

    def create(self, validated_data):
        applications_data = validated_data.pop('applications', [])  # Use 'applications' for key
        compliance = Compliance.objects.create(**validated_data)
        for app_data in applications_data:
            Application.objects.create(compliance=compliance, **app_data)
        return compliance