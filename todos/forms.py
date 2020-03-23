from django.forms import ModelForm
from .models import TodoList, Category

class ToDoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ['category', 'due_date', 'content', 'title']
