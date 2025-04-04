from django.db import models

class DynamicForm(models.Model):
    name = models.CharField(max_length=100)
    fields = models.JSONField()

class FormSubmission(models.Model):
    form = models.ForeignKey(DynamicForm, on_delete=models.CASCADE)
    data = models.JSONField()
    submitted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)