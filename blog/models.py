from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class PostManager(models.Manager):  # see https://docs.djangoproject.com/en/1.5/topics/db/managers/
    def live(self):
        return self.model.objects.filter(published=True)


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name="posts")
    category = models.CharField(max_length=127)
    objects = PostManager()  # this is for the published=True PostManager

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

    @models.permalink
    def get_absolute_url(self):
        '''
        purpose: to replace in template, this: {% url 'blog:detail' post.slug %}
                 with this: {% post.get_absolute_url %}
        This allows database-y type info to be contained to model, and don't need to mess
        with get URL from future when using Django 1.4 and earlier
        '''
        return "blog:detail", (), {"slug": self.slug}