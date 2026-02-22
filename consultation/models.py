from django.db import models

from patient.models import Patient

# Create your models here.
class Consultation(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="consultations"
    )
    symptoms = models.TextField()
    diagnosis = models.TextField(blank=True)  # optional
    created_at = models.DateTimeField(auto_now_add=True)
    ai_summary = models.TextField(null=True, blank=True)  # nullable

    def __str__(self):
        return f"Consultation for {self.patient.full_name} - {self.created_at.date()}"
