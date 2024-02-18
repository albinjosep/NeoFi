from django.core.exceptions import ValidationError

def validate_username_length(value):
    min_length = 5  # Adjust the minimum length as needed
    if len(value) < min_length:
        raise ValidationError(f'The username must be at least {min_length} characters long.')