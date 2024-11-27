from django.contrib import admin
from django.urls import path
from .views import DynamicFormView

urlpatterns = [
    path('forms/', DynamicFormView.as_view(), name= "dynamic-forms"),
]
