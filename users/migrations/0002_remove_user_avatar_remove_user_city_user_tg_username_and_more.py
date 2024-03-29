# Generated by Django 4.2.9 on 2024-02-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.AddField(
            model_name='user',
            name='tg_username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='аккаунт в телеграм'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='статус активности'),
        ),
    ]
