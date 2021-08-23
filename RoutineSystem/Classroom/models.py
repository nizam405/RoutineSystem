from django.db import models

TYPE_CHOICES = {
    ('Theory', 'Theory'),
    ('Lab', 'Lab')
}

class Classroom(models.Model):
    room = models.CharField(max_length=10)
    capacity = models.IntegerField(default=1, null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, default='Theory', max_length=6)

    def __str__(self):
        return self.room