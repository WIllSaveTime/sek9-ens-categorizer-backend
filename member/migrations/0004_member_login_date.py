# Generated by Django 3.2.3 on 2021-06-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='login_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]