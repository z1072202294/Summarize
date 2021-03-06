# Generated by Django 3.0.3 on 2020-03-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_auto_20200303_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('appid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=128)),
                ('application', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('publish_date', models.DateField()),
                ('url', models.CharField(max_length=128)),
                ('desc', models.TextField()),
            ],
        ),
    ]
