from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(null=True, blank=True)


    def __str__(self):
        return self.name


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Club.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_club_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_club_receiver, sender=Club)