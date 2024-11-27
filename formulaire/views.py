from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from formulaire.models import DynamicForm
from formulaire.serializers import DynamicFormSerializer

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
