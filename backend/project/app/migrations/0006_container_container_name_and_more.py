# Generated by Django 4.2.17 on 2024-12-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='container_name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='container_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
