# Generated by Django 4.1.1 on 2023-02-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dep', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dep',
            name='department',
        ),
    ]