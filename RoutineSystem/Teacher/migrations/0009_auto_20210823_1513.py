# Generated by Django 3.2.6 on 2021-08-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0008_auto_20210823_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.CharField(blank=True, choices=[('Instructor', 'Instructor'), ('Jr. Instructor', 'Jr. Instructor')], default='Jr. Instructor', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='technology',
            field=models.CharField(blank=True, choices=[('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Computer', 'Computer'), ('Combined', 'Combined'), ('Marine', 'Marine'), ('Mechanical', 'Mechanical')], max_length=10, null=True),
        ),
    ]
