# Generated by Django 3.0.8 on 2020-08-04 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0006_auto_20200804_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memoryitem',
            name='coordinates',
        ),
    ]
