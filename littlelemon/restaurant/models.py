from django.db import models

# Create your models here.
class Booking(models.Model):
   # ID = models.IntegerField(max = 11)
    Name = models.CharField(max_length = 255)
    No_of_guests = models.IntegerField()
    Bookingdate = models.DateTimeField()


class Menu(models.Model):
   # ID = models.IntegerField(max = 5)
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Inventory = models.PositiveIntegerField()
