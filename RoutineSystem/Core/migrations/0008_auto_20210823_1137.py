# Generated by Django 3.2.6 on 2021-08-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_auto_20210823_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['period', 'sub']},
        ),
        migrations.RemoveField(
            model_name='class',
            name='department',
        ),
        migrations.RemoveField(
            model_name='class',
            name='semester',
        ),
        migrations.AddField(
            model_name='class',
            name='shift',
            field=models.CharField(choices=[('Day', 'Day'), ('Evening', 'Evening')], default='Day', max_length=10),
        ),
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(choices=[('Mon', 'Mon'), ('Sat', 'Sat'), ('Sun', 'Sun'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Fri', 'Fri'), ('Thu', 'Thu')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='class',
            name='period_count',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double')], default='Single', max_length=10),
        ),
    ]