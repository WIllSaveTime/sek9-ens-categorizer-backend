# Generated by Django 4.0.5 on 2022-06-20 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'ordering': ('name',)},
        ),
    ]
