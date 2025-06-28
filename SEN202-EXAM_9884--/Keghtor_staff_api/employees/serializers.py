from rest_framework import serializers
from .models import Jobs, Application
from users.models import StaffBase,Manager , Intern

class serializers:
    class Meta:
        model = CompanyProfile
        fields = '__all__'
