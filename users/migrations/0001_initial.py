# Generated by Django 4.0.4 on 2022-04-23 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouletteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('money', models.FloatField()),
                ('username', models.EmailField(max_length=254)),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
    ]