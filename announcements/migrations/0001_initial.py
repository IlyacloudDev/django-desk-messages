# Generated by Django 5.0.6 on 2024-05-14 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('TA', 'Танки'), ('HE', 'Хиллы'), ('DD', 'ДД'), ('ME', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('BS', 'Кузнецы'), ('TA', 'Кожевники'), ('PM', 'Зельевары'), ('SM', 'Мастера заклинаний')], default='TA', max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=115)),
                ('announcement_text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='announcements.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='announcements.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='announcements.announcement')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='announcements.author')),
            ],
        ),
    ]
