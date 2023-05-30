# Generated by Django 4.2 on 2023-05-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pymap", "0004_remove_mappingpoint_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("content", models.TextField()),
            ],
        ),
    ]