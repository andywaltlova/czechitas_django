# Generated by Django 3.1.7 on 2021-05-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20210504_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizace',
            name='kontakt',
        ),
        migrations.AddField(
            model_name='kontakt',
            name='organizace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.organizace'),
        ),
    ]