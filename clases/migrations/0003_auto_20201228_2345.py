# Generated by Django 3.1.4 on 2020-12-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0002_auto_20201228_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='clase',
            name='autor',
            field=models.CharField(choices=[('Augusto', 'Augusto'), ('Alex', 'Alex'), ('Mani', 'Mani')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
