# Generated by Django 5.1 on 2025-01-16 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='link',
        ),
    ]
