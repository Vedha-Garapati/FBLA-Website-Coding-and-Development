# Generated by Django 5.0 on 2024-01-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_apply_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='clientInteraction',
            new_name='workExperience',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='legislationKnowledge',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='problemSolving',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='professionalDevelopment',
        ),
        migrations.RemoveField(
            model_name='apply',
            name='teamwork',
        ),
    ]
