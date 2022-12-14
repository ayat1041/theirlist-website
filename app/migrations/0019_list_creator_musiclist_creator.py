# Generated by Django 4.0 on 2022-09-22 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0018_booklist_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
        migrations.AddField(
            model_name='musiclist',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
    ]
