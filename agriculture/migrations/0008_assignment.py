# Generated by Django 5.0 on 2024-02-08 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture', '0007_remove_work_work_secondary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss_name', models.CharField(max_length=1000)),
                ('emp_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agriculture.employee')),
                ('work_primary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agriculture.work')),
            ],
        ),
    ]