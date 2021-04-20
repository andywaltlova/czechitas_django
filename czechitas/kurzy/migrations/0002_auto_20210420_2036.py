# Generated by Django 3.1.7 on 2021-04-20 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurzy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='kurz',
            name='kategorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kurzy.kategorie'),
        ),
    ]
