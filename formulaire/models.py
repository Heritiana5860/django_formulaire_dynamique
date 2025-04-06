from django.db import models

class DynamicForm(models.Model):
    name = models.CharField(max_length=100)
    fields = models.JSONField()

class FormSubmission(models.Model):
    form = models.ForeignKey(DynamicForm, on_delete=models.CASCADE, related_name='submissions')
    data = models.JSONField()
    submitted_at = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Submission for {self.form.name} at {self.submitted_at}"