# Generated by Django 3.0 on 2022-04-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220328_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='pata nhi', max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='orders',
        ),
    ]
