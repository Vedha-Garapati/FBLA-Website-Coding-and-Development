# Generated by Django 5.0 on 2023-12-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_apply_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='education',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]