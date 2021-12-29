# Generated by Django 3.2.8 on 2021-12-29 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0005_auto_20211215_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.workout')),
            ],
        ),
    ]
