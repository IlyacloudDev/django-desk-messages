# Generated by Django 5.0.6 on 2024-05-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='allowed',
            field=models.BooleanField(default=False),
        ),
    ]
