# Generated by Django 4.0.5 on 2022-06-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='subject',
            field=models.CharField(max_length=128),
        ),
    ]
