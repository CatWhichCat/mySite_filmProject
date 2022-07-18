# Generated by Django 4.0.6 on 2022-07-18 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_rewies_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Фильмы'),
        ),
        migrations.AlterField(
            model_name='rewies',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.rewies', verbose_name='Родитель'),
        ),
    ]
