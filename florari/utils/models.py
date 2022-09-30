"""Django models utilities"""

from django.db import models

class FlorAppModel(models.Model):
    """
    Flor App  base model
    This class provides every table with the following
    attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object last modified'
    )

    class Meta:
        """Meta option"""

        abstract = True

        get_latest_by = 'created'
        orderin = ['-created', '-modified']