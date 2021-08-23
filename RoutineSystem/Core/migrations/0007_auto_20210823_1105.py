# Generated by Django 3.2.6 on 2021-08-23 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subject', '0004_alter_assignedsubject_sub'),
        ('Core', '0006_auto_20210823_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(choices=[('Sun', 'Sun'), ('Thu', 'Thu'), ('Fri', 'Fri'), ('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Sat', 'Sat')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='class',
            name='department',
            field=models.CharField(choices=[('Combined', 'Combined'), ('Civil', 'Civil'), ('Computer', 'Computer'), ('Electrical', 'Electrical'), ('Mechanical', 'Mechanical'), ('Marine', 'Marine')], max_length=10),
        ),
        migrations.AlterField(
            model_name='class',
            name='semester',
            field=models.CharField(choices=[('4th', '4th'), ('7th', '7th'), ('3rd', '3rd'), ('6th', '6th'), ('8th', '8th'), ('5th', '5th'), ('1st', '1st'), ('2nd', '2nd')], max_length=3),
        ),
        migrations.AlterField(
            model_name='class',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subject.subject'),
        ),
    ]
