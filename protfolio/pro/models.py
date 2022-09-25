from django.db import models

class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/',null=True, blank=True)

    def __str__(self):
        return self.title

class ExtraModel(models.Model):
    heading = models.CharField(max_length=100,null=True, blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='projects/',null=True, blank=True)


    def __str__(self):
        return self.heading

class AchievementModel(models.Model):
    heading = models.CharField(max_length=100,null=True, blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='projects/',null=True, blank=True)
    link=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.heading