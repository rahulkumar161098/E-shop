# Generated by Django 3.0 on 2022-03-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220321_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersignup',
            old_name='username',
            new_name='u_name',
        ),
    ]
