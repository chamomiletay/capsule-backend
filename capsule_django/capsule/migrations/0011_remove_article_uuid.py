# Generated by Django 4.0.6 on 2022-07-23 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0010_article_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='uuid',
        ),
    ]