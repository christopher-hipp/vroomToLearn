import uuid

from django.db import models
from uuid import uuid4


class Car(models.Model):
    """Model representing a car, but not a specific copy of one."""
    make = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    mileage = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.make


class CarInstance(models.Model):
    """Model representing an instance of a car, e.g. a specific physical vehicle."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique id for each car")
    car = models.ForeignKey("Car", on_delete=models.RESTRICT, null=True)
    due_date = models.DateField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    RENT_STATUS = (
        ("a", "Available"),
        ("r", "Reserved"),
        ("u", "In use"),
    )

    status = models.CharField(
        max_length=1,
        choices=RENT_STATUS,
        blank=True,
        default="a",
        help_text="Car availability",
    )

    def __str__(self):
        return f"{self.car}"


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
