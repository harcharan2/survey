# Generated by Django 3.0.6 on 2020-05-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delve_form', '0003_delve_form_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delve_form',
            name='gender',
        ),
    ]
