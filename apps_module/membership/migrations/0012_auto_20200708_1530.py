# Generated by Django 3.0.7 on 2020-07-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0011_attendance_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='new_comer',
        ),
        migrations.AddField(
            model_name='member',
            name='visitor',
            field=models.BooleanField(default=False, help_text='For only visitors'),
        ),
    ]
