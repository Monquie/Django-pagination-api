# Generated by Django 5.0.1 on 2024-01-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
        migrations.AddField(
            model_name='organization',
            name='text_id',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
    ]