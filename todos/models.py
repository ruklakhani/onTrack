from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField


class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be shown when called
class TodoList(models.Model): #Todos able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field 
    created_by = CurrentUserField(null=True, blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # a foreignkey
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called
