# Generated by Django 4.2.16 on 2024-10-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='dockerfile_path',
        ),
        migrations.AddField(
            model_name='project',
            name='build_file_path',
            field=models.CharField(default='NOT SET', max_length=255),
        ),
    ]