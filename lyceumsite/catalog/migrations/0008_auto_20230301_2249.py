# Generated by Django 3.2.16 on 2023-03-01 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20230301_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='main_image',
        ),
        migrations.AddField(
            model_name='image',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.item'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='catelog/', verbose_name='1'),
        ),
    ]
