# Generated by Django 5.0 on 2024-02-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture', '0006_work_work_primary_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='work_secondary',
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_secondary_description',
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_secondary_image_field',
        ),
    ]
