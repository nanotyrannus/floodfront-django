# Generated by Django 2.2.4 on 2019-08-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
