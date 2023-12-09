from django.db import models
from django.utils import timezone
from TaskCategoryModel.models import add_category
# Create your models here.
class add_task(models.Model):
    Task_Title = models.CharField(max_length=100)
    Task_Description = models.TextField()
    Category = models.ManyToManyField(add_category)
    Task_assign_date = models.DateField(default=timezone.now, blank=True, null=True,help_text="You can Enter task assignment date or set it default now")
    Is_completed = models.BooleanField(default=False, blank=True)


    def __str__(self):
      return self.Task_Title 
