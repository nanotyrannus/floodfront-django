# Generated by Django 2.2.4 on 2019-08-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20190821_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='heading',
            field=models.FloatField(null=True),
        ),
    ]
