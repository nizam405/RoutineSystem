# Generated by Django 3.2.6 on 2021-08-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0006_auto_20210823_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(blank=True, choices=[('Mechanical', 'Mechanical'), ('Combined', 'Combined'), ('Marine', 'Marine'), ('Civil', 'Civil'), ('Computer', 'Computer'), ('Electrical', 'Electrical')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, choices=[('Jr. Instructor', 'Jr. Instructor'), ('Instructor', 'Instructor')], default='Jr. Instructor', max_length=20, null=True),
        ),
    ]
