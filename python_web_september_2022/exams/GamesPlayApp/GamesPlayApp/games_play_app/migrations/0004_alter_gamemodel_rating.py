# Generated by Django 4.1.2 on 2022-10-20 03:39

import GamesPlayApp.games_play_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_play_app', '0003_alter_gamemodel_rating_alter_gamemodel_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='rating',
            field=models.FloatField(default=0.0, validators=[GamesPlayApp.games_play_app.validators.ValueInRangeValidator(0.1, 5.0)]),
        ),
    ]
