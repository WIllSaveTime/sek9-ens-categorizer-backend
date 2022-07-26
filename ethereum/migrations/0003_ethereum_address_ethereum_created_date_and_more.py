# Generated by Django 4.0.5 on 2022-06-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum', '0002_alter_ethereum_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ethereum',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='created_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='end_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='end_price',
            field=models.DecimalField(blank=True, decimal_places=18, default=0.0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='expiry_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='label_hash',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='last_sale',
            field=models.DecimalField(blank=True, decimal_places=18, default=0.0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='owners',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='payment_token',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='registration_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='starting_price',
            field=models.DecimalField(blank=True, decimal_places=18, default=0.0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='ethereum',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
