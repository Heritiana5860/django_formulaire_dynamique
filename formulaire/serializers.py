from rest_framework import serializers
from formulaire.models import DynamicForm, FormSubmission

class DynamicFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = DynamicForm
        fields = ['id', 'name', 'fields']


class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = ['id', 'form', 'data', 'submitted_at', 'received_at']