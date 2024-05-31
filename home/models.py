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


# Social Media

class SocialMedia(models.Model):
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    def __str__(self):
        return 'Social Media'


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


# Ticket

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    crete = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.message} -{self.crete}'
