from .views import *
from django.urls import path


urlpatterns = [
    # Task 1
    path('JobView/',JobView.as_view(),name='JobView'),
    path('GetJob/',JobView.as_view(),name='Get-Job-View'),
    path('CreateApplication/',ApplicantView.as_view(),name='create-application'),
    path('GetApplication/',ApplicantView.as_view(),name='Get-application'),
    
    # Task 2
    path('ListApplicants/',JobListWithCount.as_view(),name="List-Applicant")
]
