# Generated by Django 3.2.6 on 2021-08-23 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subject', '0002_auto_20210823_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignedsubject',
            options={'ordering': ['sub']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['code']},
        ),
    ]