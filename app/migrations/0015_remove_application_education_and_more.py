# Generated by Django 5.0 on 2024-06-20 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_certify_application_certifications_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='education',
        ),
        migrations.RemoveField(
            model_name='application',
            name='middle',
        ),
        migrations.RemoveField(
            model_name='application',
            name='workExperience',
        ),
    ]
