# Generated by Django 4.2.1 on 2023-06-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_subblog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=221, null=True, unique=True),
        ),
    ]
