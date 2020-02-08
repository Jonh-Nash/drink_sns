# Generated by Django 2.2.2 on 2020-02-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0008_auto_20200118_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True, verbose_name='緯度'),
        ),
        migrations.AddField(
            model_name='diary',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='経度'),
        ),
    ]