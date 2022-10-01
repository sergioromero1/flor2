from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    """
    Extend from django's abstract User, change the username field
    to email field
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique':'Ya existe un usuario con ese email'
        }
    )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message="El numero de telefono debe ser ingresado en el formato: +529999999"
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

