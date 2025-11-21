from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# -----------------------------------------
# Car Make Model
# -----------------------------------------
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# -----------------------------------------
# Car Model Model
# -----------------------------------------
class CarModel(models.Model):

    # Many-to-one relationship: One make → many models
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    # Limited choices (required by assignment)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")

    # Year must be between 2015 and 2023
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ],
        default=2023
    )

    # Optional field: dealer ID required in the assignment
    dealer_id = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
