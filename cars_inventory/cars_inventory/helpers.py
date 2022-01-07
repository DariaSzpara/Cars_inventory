from django.core.exceptions import ValidationError


def validate_car_exists(make, model):
    if cars.model < model:
        raise ValidationError(f"Not enought cars available.")