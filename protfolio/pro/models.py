import os

import supabase as supabase
from django.db import models
from django.conf import settings


class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    githubLink=  models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/',null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            supabase_client = supabase.create_client(settings.SUPABASE_API_URL, settings.SUPABASE_API_KEY)
            if os.path.isfile(self.image.path):
                with open(self.image.path, 'rb') as file_data:
                    destination = f'{self.image.name}'
                    response = supabase_client.storage.from_('media').upload(destination, file_data)
                    if response.status_code != 200:
                    # Handle the error here
                        pass

    def __str__(self):
        return self.title

class SkillsModel(models.Model):
    heading = models.CharField(max_length=100,null=True, blank=True)
    image = models.ImageField(upload_to='Skills/', null=True, blank=True)

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

class ToolsModel(models.Model):
    heading = models.CharField(max_length=100,null=True, blank=True)
    image = models.ImageField(upload_to='Tools/', null=True, blank=True)

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
