# Generated by Django 3.0.8 on 2020-08-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0007_remove_memoryitem_coordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memoryitem',
            name='latitude',
            field=models.CharField(default=0, max_length=64),
        ),
        migrations.AlterField(
            model_name='memoryitem',
            name='longitude',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
