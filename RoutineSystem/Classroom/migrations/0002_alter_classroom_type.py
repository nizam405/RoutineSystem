# Generated by Django 3.2.6 on 2021-08-23 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='type',
            field=models.CharField(choices=[('Theory', 'Theory'), ('Lab', 'Lab')], default='Theory', max_length=6),
        ),
    ]
