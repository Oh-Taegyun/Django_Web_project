# Generated by Django 4.2 on 2023-05-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pymap", "0006_alter_reply_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactForm_E",
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
                (
                    "mbti",
                    models.CharField(choices=[("E", "E"), ("I", "I")], max_length=1),
                ),
                (
                    "influence",
                    models.CharField(
                        choices=[("yes", "예"), ("no", "아니요")], max_length=3
                    ),
                ),
                ("comments", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ContactForm_I",
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
                (
                    "mbti",
                    models.CharField(choices=[("E", "E"), ("I", "I")], max_length=1),
                ),
                (
                    "influence",
                    models.CharField(
                        choices=[("yes", "예"), ("no", "아니요")], max_length=3
                    ),
                ),
                ("comments", models.TextField()),
            ],
        ),
        migrations.DeleteModel(name="Reply",),
    ]