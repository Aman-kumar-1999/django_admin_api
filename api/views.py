from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework.decorators import action


# Create your views here.

class ComponyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)
            employeeSer = EmployeeSerializers(emp, many=True, context={'request': request})
            return Response(employeeSer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might does not exists ! error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = (Employee.objects.all())
    serializer_class = EmployeeSerializers
