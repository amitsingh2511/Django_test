# app_name/urls.py
from django.urls import path
from .views import ApplicationListCreateView, ComplianceListCreateView , ComplianceListByApplicationView ,ComplianceListWithApplicationsView

urlpatterns = [
    path('applications/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('compliances/', ComplianceListCreateView.as_view(), name='compliance-list-create'),
    path('compliances/by-application/<str:application_name>/', ComplianceListByApplicationView.as_view(), name='compliance-list-by-application'),
    path('compliances/with-applications/<str:compliance_name>/', ComplianceListWithApplicationsView.as_view(), name='compliances-with-applications'),
]
