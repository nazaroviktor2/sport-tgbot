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


class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=None, null=True, blank=True)
    weight = models.DecimalField(default=None, decimal_places=2, max_digits=5, null=True, blank=True)
    height = models.DecimalField(default=None, decimal_places=2, max_digits=5, null=True, blank=True)
    gender = models.CharField(default=None, choices=[("M", "Мужской"), ("F", "Женский"), ("M/F", "М/Ж")],
                              max_length=3, null=True, blank=True)
    lvl = models.IntegerField(default=0, null=True, blank=True)
    training_goal = models.TextField(default=None, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{0}: {1}".format(self.id, self.name)


class Dnevnik(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainings = models.ManyToManyField(Training, through="Dnevnik_trainings")

    def __str__(self):
        return "{0}: {1} , {2}".format(self.id, self.user.name, self.date)


class Dnevnik_trainings(models.Model):
    dnevnik = models.ForeignKey(Dnevnik, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    start_training = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_training = models.DateTimeField(null=True, blank=True)
