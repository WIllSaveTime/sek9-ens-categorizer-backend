# Generated by Django 4.0.5 on 2022-06-23 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0002_alter_feedback_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_sent', models.BooleanField(blank=True, default=False, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedback_fbanswers', to='feedback.feedback')),
            ],
            options={
                'db_table': 'feedback_answers',
                'ordering': ('-id',),
                'managed': True,
                'unique_together': {('id',)},
            },
        ),
    ]
