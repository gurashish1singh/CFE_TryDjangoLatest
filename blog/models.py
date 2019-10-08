from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Django in-built user model
User = settings.AUTH_USER_MODEL


# Making a generic queryset to be used everywhere, even in views
class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # get_querysets == BlogPost.objects.all()
        return self.filter(publish_date__lte=now)


# To view only published blogs!
class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self.db)

    def published(self):
        return self.get_queryset().published()


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)  # hello world > hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Initializing the class
    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title

    # To get urls for each post ( conventional)
    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    # # These are not conventional!
    # def get_edit_url(self):
    #     return f'{self.get_absolute_url}/edit'

    # # These are not conventional!
    # def get_delete_url(self):
    #     return f'{self.get_absolute_url}/delete'
