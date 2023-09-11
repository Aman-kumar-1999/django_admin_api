from rest_framework import serializers
from .models import *


class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    emp_id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
