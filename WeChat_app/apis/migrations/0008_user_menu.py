# Generated by Django 3.0.3 on 2020-03-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='menu',
            field=models.ManyToManyField(to='apis.App'),
        ),
    ]