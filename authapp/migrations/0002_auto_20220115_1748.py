# Generated by Django 3.2.9 on 2022-01-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expired',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
