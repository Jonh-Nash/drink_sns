# Generated by Django 2.2.2 on 2020-01-15 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='content',
        ),
    ]
