# Generated by Django 4.0 on 2022-09-22 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0015_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklist',
            name='creator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
