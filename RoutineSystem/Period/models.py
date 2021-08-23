from django.db import models
from django.db.models.fields import CharField

class Period(models.Model):
    num = models.IntegerField(default=0)
    start = models.TimeField(verbose_name='Start Time')
    duration = models.IntegerField(verbose_name='Duration (Minutes)')

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.num
