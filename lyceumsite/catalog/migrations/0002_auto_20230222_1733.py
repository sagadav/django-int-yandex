# Generated by Django 3.2.16 on 2023-02-22 12:33

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.TextField(
                max_length=200,
                unique=True,
                verbose_name="Артикул",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.TextField(
                max_length=200,
                unique=True,
                verbose_name="Артикул",
            ),
        ),
    ]
