# Generated by Django 3.2.6 on 2021-08-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_auto_20210823_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(choices=[('Sun', 'Sun'), ('Thu', 'Thu'), ('Wed', 'Wed'), ('Tue', 'Tue'), ('Mon', 'Mon'), ('Fri', 'Fri'), ('Sat', 'Sat')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='class',
            name='period_count',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double')], default='Single', max_length=10),
        ),
    ]
