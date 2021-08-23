from django.contrib import admin
from .models import Subject, AssignedSubject

admin.site.register(Subject)
admin.site.register(AssignedSubject)