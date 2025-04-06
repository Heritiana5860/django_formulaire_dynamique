from django.contrib import admin
from django.urls import path
from .views import DynamicFormView, FormSubmissionView

urlpatterns = [
    path('forms/', DynamicFormView.as_view(), name= "dynamic-forms"),
    path('submissions/', FormSubmissionView.as_view(), name="form-submissions"),
]
