# Generated by Django 4.1.5 on 2023-01-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=5, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский'), ('M/F', 'М/Ж')], default=None, max_length=3, null=True)),
                ('lvl', models.IntegerField(blank=True, default=0, null=True)),
                ('training_goal', models.TextField(blank=True, default=None, null=True)),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tgbot.place')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('lvl', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('M/F', 'Male/Female')], max_length=3)),
                ('type', models.CharField(choices=[('Fast', 'Быстрая'), ('Pers', 'Персональная')], default=None, max_length=255)),
                ('description', models.TextField()),
                ('muscle_group', models.CharField(choices=[('Спина', 'Спина'), ('Грудь', 'Грудь'), ('Ноги', 'Ноги'), ('Руки', 'Руки'), ('Бицепс', 'Бицепс'), ('Трицепс', 'Трицепс'), ('Трапеции', 'Трапеции'), ('Плечи', 'Плечи'), ('Пресс', 'Пресс'), ('Разминка', 'Разминка'), ('Функциональная', 'Функциональная'), ('Кардио', 'Кардио')], max_length=50)),
                ('places', models.ManyToManyField(to='tgbot.place')),
            ],
        ),
        migrations.CreateModel(
            name='Dnevnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('trainings', models.ManyToManyField(to='tgbot.training')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.user')),
            ],
        ),
    ]
