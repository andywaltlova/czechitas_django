# Generated by Django 3.1.7 on 2021-04-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('zacatek', models.DateTimeField()),
                ('konec', models.DateTimeField()),
                ('popis', models.CharField(max_length=1000)),
                ('cena', models.IntegerField()),
            ],
        ),
    ]
