from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveBigIntegerField(validators=[MaxValueValidator(999999)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.id} - {self.name}"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
