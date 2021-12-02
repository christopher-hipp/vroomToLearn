import uuid

from django.db import models
from uuid import uuid4


"""class Make(models.Model):
    make = models.CharField(max_length=100)

    def __str__(self):
        return self.make"""


class Car(models.Model):
    """Model representing a car, but not a specific copy of one."""
    make = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    mileage = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.make


class CarInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique id for each car")
    car = models.ForeignKey("Car", on_delete=models.RESTRICT, null=True)
    due_date = models.DateField(null=True, blank=True)


