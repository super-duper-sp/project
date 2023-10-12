from django.db import models

import supabase as supabase
from django.conf import settings

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

class AboutModel(models.Model):
    heading= models.CharField(max_length=100,null=True, blank=True)
    heading2 = models.CharField(max_length=100, null=True, blank=True)
    heading3 = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    resumeLink=models.TextField(null=True, blank=True)
    hireLink= models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='About/', null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            supabase_client = supabase.create_client(settings.SUPABASE_API_URL, settings.SUPABASE_API_KEY)
            with open(self.image.path, 'rb') as file_data:
                destination = f'{self.image.name}'
                response = supabase_client.storage.from_('media').upload(destination, file_data)
                if response.status_code != 200:
                    # Handle the error here
                    pass

    def __str__(self):
        return self.heading



