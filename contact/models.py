from django.db import models

# Create your models here.
# after creating any new model we need to make migrations


class ContactDetails(models.Model):
    # location = models
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)
