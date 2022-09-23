from django.db import models

class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/',null=True, blank=True)

    def __str__(self):
        return self.title