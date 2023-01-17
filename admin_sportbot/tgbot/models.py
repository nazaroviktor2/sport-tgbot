from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Place(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Training(models.Model):
    muscle_groups = [
        ("Спина", "Спина"),
        ("Грудь", "Грудь"),
        ("Ноги", "Ноги"),
        ("Руки", "Руки"),
        ("Бицепс", "Бицепс"),
        ("Трицепс", "Трицепс"),
        ("Трапеции", "Трапеции"),
        ("Плечи", "Плечи"),
        ("Пресс", "Пресс"),
        ("Разминка", "Разминка"),
        ("Функциональная", "Функциональная"),
        ("Кардио", "Кардио")
    ]
    name = models.TextField()
    lvl = models.IntegerField(default=0, null=False)
    gender = models.CharField(choices=[("M", "Male"), ("F", "Female"), ("M/F", "Male/Female")], max_length=3)
    type = models.CharField(default=None, max_length=255, choices=[("Fast", "Быстрая"), ("Pers", "Персональная")])
    description = models.TextField(null=False)
    muscle_group = models.CharField(null=False, choices=muscle_groups, max_length=50)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.name


class User(AbstractUser):
    age = models.IntegerField(default=None, null=True, blank=True)
    weight = models.DecimalField(default=None, decimal_places=2, max_digits=4, null=True, blank=True)
    height = models.DecimalField(default=None, decimal_places=2, max_digits=4, null=True, blank=True)
    gender = models.CharField(default=None, choices=[("M", "Мужской"), ("F", "Женский"), ("M/F", "М/Ж")],
                              max_length=3, null=True, blank=True)
    lvl = models.IntegerField(default=0, null=True, blank=True)
    training_goal = models.TextField(default=None, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
