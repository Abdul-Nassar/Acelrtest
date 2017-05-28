from django.db import models

# Create your models here.

def built_image(self, filename):
    """ image handler function for global menu item image
    """
    url = "uploads/builtby/%s" % (filename)
    return url

class BuiltBy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=built_image, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Repositories(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    rating = models.FloatField()
    connections = models.IntegerField()
    language = models.CharField(max_length=255, blank=True, null=True)
    built_by = models.ManyToManyField(BuiltBy, blank=True)

    def __unicode__(self):
        return self.title
