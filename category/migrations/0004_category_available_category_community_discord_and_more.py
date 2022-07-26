# Generated by Django 4.0.5 on 2022-06-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='available',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='community_discord',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='category',
            name='community_twitter',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='files',
            field=models.CharField(blank=True, default=None, max_length=1024),
        ),
        migrations.AddField(
            model_name='category',
            name='floor',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.CharField(blank=True, default=None, max_length=1024),
        ),
        migrations.AddField(
            model_name='category',
            name='owners',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='regular_expression',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AddField(
            model_name='category',
            name='short_name',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='category',
            name='wiki_url',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
    ]
