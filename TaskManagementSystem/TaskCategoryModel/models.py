from django.db import models

# Create your models here.
class add_category(models.Model):
    Category_Name = models.CharField(max_length=150)

    def __str__(self):
        return self.Category_Name 