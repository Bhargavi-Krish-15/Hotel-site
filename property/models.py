from django.db import models

# Create your models here.

# For our main project we are supposed to have various models which we need to include in and those models will have various field and its properties that we want to initialize and include, this is the space for it.
# This will create a table for it by doing migrations. make sure to define it in setting.py as well - in the installed app section


property_type = {
    ('S', "sale"),
    ('R', "rent")
}


class Property(models.Model):
    # name
    # type can be sale or rent
    # area
    # price
    # beds number
    # bath number
    # garage numebr

    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    area = models.DecimalField(decimal_places=2, max_digits=8)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    bed_count = models.PositiveIntegerField()
    bath_count = models.PositiveIntegerField()
    garage_count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True)
    location = models.CharField(max_length=50, null=True)

    # this is for admin side- if we wanted to display the name of the object instaead of a random alphabets.
    def __str__(self):
        return self.name

    # this is also admin side how do u want to dispaly the name in plural
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Rooms"

# wanted a category of which type or room it is


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Room Categories"


# now we wanted to reserve the rooms
class Reserve(models.Model):
    # we want info of who is booking
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name
