# Generated by Django 4.2.2 on 2023-06-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnimalFacts",
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
                ("info", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="CapitalFacts",
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
                ("info", models.CharField(max_length=200)),
            ],
        ),
    ]
