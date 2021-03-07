# Generated by Django 3.1.7 on 2021-03-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='couponsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allotedTo', models.CharField(max_length=30)),
                ('allocationStatus', models.CharField(choices=[('Using', 'Using'), ('Submitted', 'Submitted')], default='Not Alloted', max_length=30)),
                ('venderID', models.CharField(max_length=30)),
                ('venderName', models.CharField(max_length=30)),
                ('venderStatus', models.CharField(choices=[('Recieved', 'Recieved'), ('Not Recieved', 'Not Recieved'), ('Processing', 'Processing')], default='Not Recieved', max_length=30)),
            ],
        ),
    ]
