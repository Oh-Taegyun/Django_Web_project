# Generated by Django 4.2 on 2023-05-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pymap", "0003_mappingpoint_delete_mappingresult"),
    ]

    operations = [
        migrations.RemoveField(model_name="mappingpoint", name="created_at",),
    ]
