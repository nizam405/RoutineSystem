from django.db import models

from Classroom.models import Classroom
from Period.models import Period
from Subject.models import AssignedSubject
from .choices import DAY_CHOICES, PERIOD_CHOICES

class Class(models.Model):
    day             = models.CharField(max_length=15, choices=DAY_CHOICES, default="")
    period          = models.ForeignKey(to=Period, on_delete=models.SET_NULL, null=True, blank=True)
    period_count    = models.CharField(max_length=10, choices=PERIOD_CHOICES, default="Single")
    sub             = models.ForeignKey(to=AssignedSubject, on_delete=models.SET_NULL, null=True, blank=True)
    classroom       = models.ForeignKey(to=Classroom, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['period', 'sub']
        verbose_name_plural = "Classes"

    def __str__(self):
        return f"{self.department} - {self.semester} - {self.sub.code}"
