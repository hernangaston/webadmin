# Generated by Django 2.1.5 on 2019-03-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chofer', '0002_auto_20190328_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='patente_acoplado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='patente_chasis',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
