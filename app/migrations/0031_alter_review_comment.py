# Generated by Django 4.0 on 2022-10-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_musiclist_spoiler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]