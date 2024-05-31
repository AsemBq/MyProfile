from django.db import models


# header

class Header(models.Model):
    name = models.CharField(max_length=75)
    position = models.CharField(max_length=75)
    img = models.ImageField('img/home')

    def __str__(self):
        return 'Header'


# About Me section

class AboutMe(models.Model):
    info = models.TextField()
    email = models.CharField(max_length=95)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return 'About Me'


# Tecnology


class Technology(models.Model):
    img = models.ImageField('img/Technology')
    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} - {self.level}'


# Tools

class Tools(models.Model):
    img = models.ImageField('img/Tools')
    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} - {self.level}'


# Other Skills

class OtherSkills(models.Model):
    tittle = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.tittle}'


# Projects

class Project(models.Model):
    img = models.ImageField('img/Project')
    tittle = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    tech = models.ManyToManyField(Technology)
    code = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tittle}'
