from django.db import models

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name