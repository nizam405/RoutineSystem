# Generated by Django 3.2.6 on 2021-08-23 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subject', '0003_auto_20210823_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedsubject',
            name='sub',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Subject.subject'),
        ),
    ]
