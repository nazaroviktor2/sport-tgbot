# Generated by Django 4.1.5 on 2023-02-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0006_rename_dnevnik_training_dnevnik_trainings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnevnik_trainings',
            name='end_training',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='dnevnik_trainings',
            name='start_training',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
