# Generated by Django 5.1 on 2024-08-15 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_home', models.CharField(max_length=64)),
                ('home_text', models.TextField()),
                ('c_eat', models.CharField(max_length=64)),
                ('eat_text', models.TextField()),
                ('c_med', models.CharField(max_length=64)),
                ('med_text', models.TextField()),
                ('c_toy', models.CharField(max_length=64)),
                ('toy_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_home', models.CharField(max_length=64)),
                ('hometext', models.TextField()),
                ('d_eat', models.CharField(max_length=64)),
                ('eattext', models.TextField()),
                ('d_med', models.CharField(max_length=64)),
                ('medtext', models.TextField()),
                ('d_toy', models.CharField(max_length=64)),
                ('toytext', models.TextField()),
            ],
        ),
    ]
