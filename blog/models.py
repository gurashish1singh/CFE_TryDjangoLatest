from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True) # hello world > hello-world
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title