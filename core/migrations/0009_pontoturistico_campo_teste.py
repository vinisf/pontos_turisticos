# Generated by Django 2.0.4 on 2018-04-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pontoturistico_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='campo_teste',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
