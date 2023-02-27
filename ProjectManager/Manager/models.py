from django.db import models

# Create your models here.

class Manager(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(default="", null=False)
    image = models.ImageField(upload_to="Images")
    link = models.CharField(max_length=250)
    publish_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']

def __str__(self):
    return self.name

