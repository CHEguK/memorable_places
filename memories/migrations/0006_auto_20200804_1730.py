# Generated by Django 3.0.8 on 2020-08-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0005_memoryitem_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='memoryitem',
            name='latitude',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memoryitem',
            name='longitude',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
