# Generated by Django 3.0.2 on 2020-02-16 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0016_auto_20200213_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='theme',
            field=models.CharField(choices=[('BOOTSTRAP', 'Bootstrap'), ('DARKLY', 'Darkly'), ('FLATLY', 'Flatly'), ('SUPERHERO', 'Superhero')], default='FLATLY', max_length=128),
        ),
    ]
