from django.db import models
from django.db.models.fields import CharField
from Core.choices import TECHNOLOGY_CHOICES

DESIGNATION_CHOICES = {
    ('Instructor','Instructor'),
    ('Jr. Instructor','Jr. Instructor'),
}

class Teacher(models.Model):
    name        = models.CharField(max_length=50)
    phone       = models.CharField(max_length=11, default="", blank=True, null=True)
    technology  = models.CharField(max_length=10, choices=TECHNOLOGY_CHOICES, blank=True, null=True)
    designation = CharField(max_length=20, default="Jr. Instructor", choices=DESIGNATION_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ['technology','name']

    def __str__(self):
        return self.name + " - " + str(self.phone) + " - " + str(self.designation)
