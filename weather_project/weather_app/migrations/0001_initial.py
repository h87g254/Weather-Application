# Generated by Django 5.1.2 on 2024-10-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
