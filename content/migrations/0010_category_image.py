# Generated by Django 5.1.4 on 2025-04-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_author_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='categories'),
        ),
    ]
