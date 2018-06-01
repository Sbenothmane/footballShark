# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-18 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_1', models.IntegerField(default=0)),
                ('score_2', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GameBet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_val', models.IntegerField()),
                ('ou_val', models.IntegerField()),
                ('line_bet', models.IntegerField()),
                ('ou_bet', models.IntegerField()),
                ('bet_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.BetSet')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Game')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='league',
            name='members',
            field=models.ManyToManyField(to='app.Person'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='app.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='app.Team'),
        ),
        migrations.AddField(
            model_name='betset',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.League'),
        ),
        migrations.AddField(
            model_name='betset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Person'),
        ),
    ]
