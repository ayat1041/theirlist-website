# Generated by Django 4.0 on 2022-09-07 08:22

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_list_desc_remove_list_desc10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='content',
            field=froala_editor.fields.FroalaField(default=' ', null=True),
        ),
    ]
