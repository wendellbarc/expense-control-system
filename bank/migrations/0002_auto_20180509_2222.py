# Generated by Django 2.0.5 on 2018-05-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='number',
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='acc_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='bank_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='agency',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
