# Generated by Django 4.0 on 2022-09-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_booklist_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True),
        ),
    ]