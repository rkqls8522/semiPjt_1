# Generated by Django 3.2.13 on 2022-11-04 02:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='unlike_users',
            field=models.ManyToManyField(related_name='unlike_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
