import supabase as supabase
from django.db import models
from django.conf import settings

# Create your models here.
from django.db import models


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    for_showcase = models.TextField(max_length=400,null=True, blank=True)
    img = models.ImageField(upload_to='post/',null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.img:
            supabase_client = supabase.create_client(settings.SUPABASE_API_URL, settings.SUPABASE_API_KEY)
            with open(self.img.path, 'rb') as file_data:
                destination = f'{self.img.name}'
                response = supabase_client.storage.from_('media').upload(destination, file_data)
                if response.status_code != 200:
                    # Handle the error here
                    pass

    def __str__(self):
        return self.title
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
