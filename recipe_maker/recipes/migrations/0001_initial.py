# Generated by Django 4.2 on 2024-04-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('foodDescription', models.CharField(max_length=500)),
                ('recipe', models.CharField(max_length=500)),
                ('ingredients', models.ManyToManyField(to='recipes.ingredient')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
