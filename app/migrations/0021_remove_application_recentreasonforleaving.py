# Generated by Django 5.0 on 2024-06-24 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_reasonforapplying_application_whytheywanttojoin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='recentReasonForLeaving',
        ),
    ]