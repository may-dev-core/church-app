# Generated by Django 3.0.7 on 2020-07-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_member_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='visitor',
        ),
        migrations.AddField(
            model_name='member',
            name='new_comer',
            field=models.BooleanField(default=False, help_text='For only New members'),
        ),
    ]
