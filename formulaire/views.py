from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from formulaire.models import DynamicForm, FormSubmission
from formulaire.serializers import DynamicFormSerializer, FormSubmissionSerializer

class DynamicFormView(APIView):
    def get(self, request):
        forms = DynamicForm.objects.all()
        serializer = DynamicFormSerializer(forms, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = DynamicFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
class FormSubmissionView(APIView):
    def post(self, request):
        serializer = FormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        form_id = request.query_params.get('form')
        if form_id:
            submissions = FormSubmission.objects.filter(form_id=form_id)
        else:
            submissions = FormSubmission.objects.all()
        serializer = FormSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)