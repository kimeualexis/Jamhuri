from django.db import models
from django.utils import timezone


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    staff_img = models.FileField()
    staff_desc = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()
    image = models.FileField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=30)
    hod = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30)
    patron = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Mission(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Vision(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Anthem(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Motto(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=45)
    date = models.DateField(default=timezone.now)
    image = models.FileField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.subject


class Coach(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Sport(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    desc = models.TextField(default=1)

    def __str__(self):
        return self.name
