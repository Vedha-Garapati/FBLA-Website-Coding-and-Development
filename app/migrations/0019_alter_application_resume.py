# Generated by Django 5.0 on 2024-06-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_application_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='user_directory_path'),
        ),
    ]
