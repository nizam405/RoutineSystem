# Generated by Django 3.2.6 on 2021-08-23 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Period', '0001_initial'),
        ('Classroom', '0002_alter_classroom_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('6th', '6th'), ('8th', '8th'), ('3rd', '3rd'), ('5th', '5th'), ('7th', '7th'), ('2nd', '2nd'), ('4th', '4th'), ('1st', '1st')], max_length=3)),
                ('department', models.CharField(choices=[('Electrical', 'Electrical'), ('Computer', 'Computer'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'), ('Marine', 'Marine'), ('Combined', 'Combined')], max_length=10)),
                ('period_count', models.IntegerField(default=1)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Classroom.classroom')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Period.period')),
            ],
        ),
    ]