# Generated by Django 3.2.16 on 2023-02-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20230223_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='normalized_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Нормализированное название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='normalized_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Нормализированное название'),
        ),
    ]