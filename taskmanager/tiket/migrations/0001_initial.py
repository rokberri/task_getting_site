# Generated by Django 5.0.7 on 2024-08-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.TextField()),
                ('body', models.TextField()),
                ('status', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
