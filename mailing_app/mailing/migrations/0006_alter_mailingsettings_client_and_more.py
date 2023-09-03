# Generated by Django 4.2.4 on 2023-09-01 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_rename_settigns_mailinglogs_settings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingsettings',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.client'),
        ),
        migrations.AlterField(
            model_name='mailingsettings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing.mailingsettings'),
        ),
    ]