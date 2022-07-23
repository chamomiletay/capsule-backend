# Generated by Django 4.0.6 on 2022-07-23 08:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0011_remove_article_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True),
        ),
    ]
