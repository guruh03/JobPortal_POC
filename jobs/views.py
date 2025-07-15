from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class JobView(APIView):
    """Task 1"""
    def post(self, request):
        
        data = request.data
        
        serializer = CreateJobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        
            payload = {
                "status": True,
                "message": "Job application submitted succesfully !!",
                "data": serializer.data,
                "error": None
            }
            return Response(payload, status=status.HTTP_201_CREATED)
            
        else:
            payload = {
                "status": False,
                "message": "Job application failed",
                "data": None,
                "error": serializer.errors
            }
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        
        id = request.query_params.get("job_id", None)
        
        if id:
            try:
                jobObj = JobPost.objects.get(id=id)
            except JobPost.DoesNotExist as e:
                payload = {
                    "status": False,
                    "message": "Job application not found",
                    "data": None,
                    "error": str(e)
                }
                return Response(payload, status=status.HTTP_404_NOT_FOUND)
            
            serializer = GetJobSerializer(jobObj).data
            payload = {
                "status": True,
                "message": "Job application fetched succesfully !!",
                "data": serializer,
                "error": None
            }
            return Response(payload, status=status.HTTP_200_OK)
        
        else:
            jobObj = JobPost.objects.all()
            if not jobObj.exists():
                payload = {
                    "status": False,
                    "message": "No Job applications found",
                    "data": None,
                    "error": "Application not found"
                }
                return Response(payload, status=status.HTTP_404_NOT_FOUND)
        
            serializer = GetJobSerializer(jobObj, many=True).data
            payload = {
                "status": True,
                "message": "Job application fetched succesfully !!",
                "data": serializer,
                "error": None
            }
            return Response(payload, status=status.HTTP_200_OK)
            
class ApplicantView(APIView):
    """Task 2"""
    def post(self, request):
        data = request.data
        
        name = data.get("name")
        email = data.get("email")
        resumeLink = data.get("resume_link")
        appliedJob = data.get("applied_job")
        
        today = timezone.now().date()
        
        try:
            jobObj = JobPost.objects.get(id=appliedJob)
        except JobPost.DoesNotExist as e:
            payload = {
                "status": False,
                "message": "Job application not found",
                "data": None,
                "error": str(e)
            }
            return Response(payload, status=status.HTTP_404_NOT_FOUND)    
        
        ################ Task 3 ##################
        applicantQset = Applicant.objects.filter(email=email, applied_at__date=today).count()
        
        """Task 3"""
        if applicantQset >=3:
            payload = {
                "status": False,
                "message": "Job application has been closed for the day",
                "data": None,
                "error": "You can apply for a maximum of 3 jobs per day"
            }
            return Response(payload, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        applicant = Applicant.objects.create(
            name=name,
            email=email,
            resume_link=resumeLink,
            applied_job=jobObj
        )
        
        serializer = GetApplicantSerializer(applicant).data
        jobserialiser = GetJobSerializer(jobObj).data
        
        payload = {
            "status": True,
            "message": "Job application submitted succesfully",
            "applicant_details": serializer,
            "job_detail": jobserialiser,
            "error": None
        }
        return Response(payload, status=status.HTTP_201_CREATED)
            
    def get(self, request):
        
        id = request.query_params.get("applicant_id", None)
        
        if id:
            try:
                applicantObj = Applicant.objects.get(id=id)
            except Applicant.DoesNotExist as e:
                payload = {
                    "status": False,
                    "message": "Job application not found",
                    "data": None,
                    "error": str(e)
                }
                return Response(payload, status=status.HTTP_404_NOT_FOUND)
            
            
            applicantSerializer = GetApplicantSerializer(applicantObj).data
            
            payload = {
                "status": True,
                "message": "Job application fetched succesfully !!",
                "applicant_details": applicantSerializer,
                "error": None
            }
            return Response(payload, status=status.HTTP_200_OK)
        
        else:
            applicantObj = Applicant.objects.all()
            if not applicantObj.exists():
                payload = {
                    "status": False,
                    "message": "No Job applications found",
                    "data": None,
                    "error": "Application not found"
                }
                return Response(payload, status=status.HTTP_404_NOT_FOUND)
        
            applicantSerializer = GetApplicantSerializer(applicantObj, many=True).data
            
            payload = {
                "status": True,
                "message": "Job application fetched succesfully !!",
                "data": applicantSerializer,
                "error": None
            }
            return Response(payload, status=status.HTTP_200_OK)

class JobListWithCount(APIView):
    """Task 2"""
    def get(self, request):
        jobs = JobPost.objects.all()
        jobList = []

        for job in jobs:
            count = Applicant.objects.filter(applied_job=job).count()
            jobList.append({
                "id": job.id,
                "title": job.title,
                "location": job.location,
                "posted_by": job.posted_by,
                "created_at": job.created_at,
                "applicant_count": count
            })

        jobList.sort(key=lambda x: x['applicant_count'], reverse=True)

        return Response(jobList, status=status.HTTP_200_OK)
            