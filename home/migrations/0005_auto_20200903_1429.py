# Generated by Django 2.2.16 on 2020-09-03 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_number', models.PositiveIntegerField()),
                ('episode_description', models.TextField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode_season', to='home.Season')),
                ('tags', models.ManyToManyField(related_name='episode_tags', to='home.Season')),
            ],
        ),
        migrations.AddField(
            model_name='podcaster',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='podcaster_tags', to='home.Episode'),
        ),
    ]