# Generated by Django 4.1.2 on 2022-10-19 13:23

import GamesPlayApp.games_play_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_play_app', '0002_create_games_and_profile_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='rating',
            field=models.FloatField(default=0.1, validators=[GamesPlayApp.games_play_app.validators.ValueInRangeValidator(0.1, 5.0)]),
        ),
        migrations.AlterField(
            model_name='gamemodel',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(12)]),
        ),
    ]
