# Generated by Django 3.0.7 on 2020-07-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_auto_20200705_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.AutoField(help_text='Auto generated, do not change!', primary_key=True, serialize=False, unique=True),
        ),
    ]
