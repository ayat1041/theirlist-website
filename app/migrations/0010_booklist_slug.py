# Generated by Django 4.0 on 2022-09-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_booklist_type_list_type_musiclist_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklist',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]