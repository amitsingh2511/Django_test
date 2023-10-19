# api/views.py
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Application, Compliance
from .serializers import ApplicationSerializer, ComplianceSerializer

class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ComplianceListCreateView(generics.ListCreateAPIView):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer

class ComplianceListByApplicationView(generics.ListAPIView):
    serializer_class = ComplianceSerializer

    def get_queryset(self):
        application_name = self.kwargs['application_name']
        print(f"Application Name: {application_name}")
        queryset = Compliance.objects.filter(applications__application_name=application_name)
        print(str(queryset.query))
        return queryset

class ComplianceListWithApplicationsView(ListAPIView):
    serializer_class = ComplianceSerializer

    def get_queryset(self):
        compliance_name = self.kwargs['compliance_name']
        return Compliance.objects.filter(name=compliance_name)