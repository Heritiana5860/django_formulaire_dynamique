from rest_framework import serializers
from formulaire.models import DynamicForm

class DynamicFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = DynamicForm
        fields = ['name', 'fields']