# Generated by Django 3.0 on 2022-05-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20220411_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]