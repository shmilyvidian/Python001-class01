# Generated by Django 2.2.13 on 2020-08-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sign', '0003_auto_20200826_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]