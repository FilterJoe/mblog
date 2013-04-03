from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name="posts")

    class Meta:
        ordering = ["-created_at", "title"]  # descending order indicated by "-" in front of created_at
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        override save to add default slug, if no slug is specified
        :param args:
        :param kwargs:
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)