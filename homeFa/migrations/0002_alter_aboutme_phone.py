# Generated by Django 5.0.6 on 2024-05-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeFa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
