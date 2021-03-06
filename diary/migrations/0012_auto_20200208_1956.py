# Generated by Django 2.2.2 on 2020-02-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0011_auto_20200208_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True, verbose_name='緯度'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='経度'),
        ),
    ]
