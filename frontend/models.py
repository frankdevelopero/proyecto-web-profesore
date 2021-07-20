from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(null=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    ammount = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="pictures")
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.user.user.first_name


class Bookin(models.Model):
    ammount = models.FloatField()
    studen = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    bookint_to = models.DateTimeField()
    payment_method = models.IntegerField()
    bookint_at = models.DateField(auto_now_add=True)
