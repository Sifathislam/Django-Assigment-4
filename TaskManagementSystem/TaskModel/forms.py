from django import forms
from .models import add_task

class TaskForm(forms.ModelForm):
    class Meta:
        model = add_task
        fields = '__all__'