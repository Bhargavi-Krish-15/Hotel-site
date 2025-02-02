from django.db import models

# Create your models here.
#after creating any new model we need to make migrations
class Agent(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/')

    def __str__(self):
        return self.name
    