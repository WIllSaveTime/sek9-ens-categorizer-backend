# Generated by Django 4.0.5 on 2022-06-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='priority',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]