# Generated by Django 3.2.8 on 2021-12-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
    ]