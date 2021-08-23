from django.db import models
from Teacher.models import Teacher
from Core.choices import SEMESTER_CHOICES, TECHNOLOGY_CHOICES, SHIFT_CHOICES


class Subject(models.Model):
    curriculumn = models.CharField(max_length=4, default='2016')
    semester = models.CharField(max_length=3, choices=SEMESTER_CHOICES, null=True, blank=True)
    technology = models.CharField(max_length=15, choices=TECHNOLOGY_CHOICES, null=True, blank=True, default="Combined")
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    t = models.IntegerField(blank=True, null=True)
    p = models.IntegerField(blank=True, null=True)
    c = models.IntegerField(blank=True, null=True)
    t_cont_assess = models.IntegerField(blank=True, null=True)
    t_final = models.IntegerField(blank=True, null=True)
    p_cont_asses = models.IntegerField(blank=True, null=True)
    p_final = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['semester', 'technology', 'code']
        

    def __str__(self):
        string = f"{self.code} - {self.name}"
        return string


class AssignedSubject(models.Model):
    shift   = models.CharField(max_length=10, choices=SHIFT_CHOICES, default="Day")
    sub     = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['sub']

    def __str__(self):
        string = f"({self.sub.code}) {self.sub.name} - "
        string += self.teacher.name if self.teacher != None else ""
        return string
