# Generated by Django 3.2.6 on 2021-08-23 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_class_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='department',
            field=models.CharField(choices=[('Computer', 'Computer'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'), ('Marine', 'Marine'), ('Combined', 'Combined'), ('Electrical', 'Electrical')], max_length=10),
        ),
        migrations.AlterField(
            model_name='class',
            name='semester',
            field=models.CharField(choices=[('3rd', '3rd'), ('5th', '5th'), ('1st', '1st'), ('6th', '6th'), ('8th', '8th'), ('7th', '7th'), ('2nd', '2nd'), ('4th', '4th')], max_length=3),
        ),
    ]