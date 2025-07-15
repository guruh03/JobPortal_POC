from .models import *
from rest_framework import serializers


class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'

class GetJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'
        
class CreateApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
        
class GetApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
        
        