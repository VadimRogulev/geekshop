# Generated by Django 3.2.9 on 2022-01-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_shopuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuserprofile',
            name='aboutMe',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='о себе'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'М'), ('W', 'Ж'), ('U', 'Н')], default='U', max_length=1, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='tagline',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='теги'),
        ),
    ]