# Generated by Django 3.2.6 on 2021-08-23 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(blank=True, default=1, null=True)),
                ('type', models.CharField(choices=[('Lab', 'Lab'), ('Theory', 'Theory')], default='Theory', max_length=6)),
            ],
        ),
    ]
