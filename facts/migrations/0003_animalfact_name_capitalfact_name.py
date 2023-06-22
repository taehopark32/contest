# Generated by Django 4.2.2 on 2023-06-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facts", "0002_rename_capitalfacts_animalfact_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animalfact",
            name="name",
            field=models.CharField(default="animal", max_length=200),
        ),
        migrations.AddField(
            model_name="capitalfact",
            name="name",
            field=models.CharField(default="capital", max_length=200),
        ),
    ]