# Generated by Django 4.2.2 on 2023-06-20 20:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facts", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CapitalFacts",
            new_name="AnimalFact",
        ),
        migrations.RenameModel(
            old_name="AnimalFacts",
            new_name="CapitalFact",
        ),
    ]
