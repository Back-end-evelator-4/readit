# Generated by Django 4.2.1 on 2023-06-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_created_date_blog_modifate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subblog',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
