# Generated by Django 3.0.6 on 2020-12-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proba1', '0010_documento_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='Cuenta',
            field=models.BigIntegerField(null=True, verbose_name='Cuenta'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='Gen',
            field=models.IntegerField(null=True),
        ),
    ]