# Generated by Django 3.0 on 2022-03-21 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_signup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUp',
            new_name='UserSignUp',
        ),
    ]
