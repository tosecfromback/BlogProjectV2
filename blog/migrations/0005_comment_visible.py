# Generated by Django 4.2.3 on 2023-07-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
