# Generated by Django 3.2.16 on 2023-01-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20230108_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
