# Generated by Django 5.0.4 on 2024-04-25 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierating', '0008_remove_rating_movieid_remove_rating_userid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('releaseDate', models.DateTimeField()),
                ('authorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movierating.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movierating.genre')),
                ('regieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movierating.regie')),
            ],
        ),
    ]
