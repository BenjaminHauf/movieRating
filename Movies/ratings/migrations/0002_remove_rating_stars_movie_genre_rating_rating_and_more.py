# Generated by Django 5.0.4 on 2024-04-18 14:03

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='stars',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
