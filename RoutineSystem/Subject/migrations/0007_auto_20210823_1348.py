# Generated by Django 3.2.6 on 2021-08-23 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0008_auto_20210823_1348'),
        ('Subject', '0006_auto_20210823_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['semester', 'technology', 'code']},
        ),
        migrations.RemoveField(
            model_name='subject',
            name='department',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.AddField(
            model_name='subject',
            name='curriculumn',
            field=models.CharField(default='2016', max_length=4),
        ),
        migrations.AddField(
            model_name='subject',
            name='technology',
            field=models.CharField(blank=True, choices=[('Mechanical', 'Mechanical'), ('Combined', 'Combined'), ('Marine', 'Marine'), ('Computer', 'Computer'), ('Civil', 'Civil'), ('Electrical', 'Electrical')], default='Combined', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(blank=True, choices=[('1st', '1st'), ('7th', '7th'), ('2nd', '2nd'), ('8th', '8th'), ('5th', '5th'), ('4th', '4th'), ('3rd', '3rd'), ('6th', '6th')], max_length=3, null=True),
        ),
        migrations.CreateModel(
            name='AssignedSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Evening', 'Evening')], default='Day', max_length=10)),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subject.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Teacher.teacher')),
            ],
            options={
                'ordering': ['sub'],
            },
        ),
    ]