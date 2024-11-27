from django.db import models

class DynamicForm(models.Model):
    name = models.CharField(max_length=100)
    fields = models.JSONField()
