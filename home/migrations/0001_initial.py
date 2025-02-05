# Generated by Django 5.0.6 on 2024-05-31 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('email', models.CharField(max_length=95)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=75)),
                ('position', models.CharField(max_length=75)),
                ('img', models.ImageField(upload_to='', verbose_name='img/home')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('telegram', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
        ),
    ]
