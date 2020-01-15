# Generated by Django 2.2.2 on 2020-01-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20200115_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='restaurant',
            field=models.CharField(max_length=100, null=True, verbose_name='店名'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='station',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='最寄り駅'),
        ),
    ]
