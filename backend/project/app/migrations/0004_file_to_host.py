# Generated by Django 4.2.16 on 2024-11-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_project_dockerfile_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='to_host',
            field=models.BooleanField(default=False),
        ),
    ]