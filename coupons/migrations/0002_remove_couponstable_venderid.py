# Generated by Django 3.1.7 on 2021-03-07 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='couponstable',
            name='venderID',
        ),
    ]
