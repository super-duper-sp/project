from django.db import models

class MessageModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SocialModel(models.Model):
    heading = models.CharField(max_length=100)
    about = models.TextField()
    logo = models.ImageField(upload_to='social/')


class EducationModel(models.Model):
    heading = models.CharField(max_length=100,null=True, blank=True)
    year = models.CharField(max_length=100)
    description = models.TextField()
    institute = models.CharField(max_length=50)

    def __str__(self):
        return self.heading

class ExperienceModel(models.Model):
    heading = models.CharField(max_length=100,null=True, blank=True)
    year = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.heading


