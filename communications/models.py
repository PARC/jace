# Create your models here.
"""
Main API Code
Joel Schooler
"""
from django.contrib.postgres import fields
from django.db import models

from user_model.updates import update_all

UUID_FIELD = 36
SHORT_LENGTH = 200
MEDIUM_LENGTH = 1024
LONG_LENGTH = 2048
SUPER_LONG = 9000
DBZ_LENGTH = 32365


class FittleReport(models.Model):
    _id = models.CharField(max_length=UUID_FIELD, primary_key=True)
    studyName = models.CharField(max_length=MEDIUM_LENGTH)
    kind = models.CharField(max_length=MEDIUM_LENGTH)
    source = models.CharField(max_length=SHORT_LENGTH)
    data = fields.JSONField()
    shared = fields.JSONField()
    createdAt = models.CharField(max_length=SHORT_LENGTH)
    def __repr__(self):
        return str(self._id)


class debugReport(models.Model):
    studyName = models.CharField(max_length=MEDIUM_LENGTH)
    kind = models.CharField(max_length=MEDIUM_LENGTH)
    data = fields.JSONField()
    source = models.CharField(max_length=SHORT_LENGTH)
    def __repr__(self):
        return str(self.data)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        for field in self._meta.concrete_fields:
            if field.is_relation:
                # If the related field isn't cached, then an instance hasn't
                # been assigned and there's no need to worry about this check.
                try:
                    getattr(self, field.get_cache_name())
                except AttributeError:
                    continue
                obj = getattr(self, field.name, None)
                # A pk may have been assigned manually to a model instance not
                # saved to the database (or auto-generated in a case like
                # UUIDField), but we allow the save to proceed and rely on the
                # database to raise an IntegrityError if applicable. If
                # constraints aren't supported by the database, there's the
                # unavoidable risk of data corruption.
                if obj and obj.pk is None:
                    # Remove the object from a related instance cache.
                    if not field.remote_field.multiple:
                        delattr(obj, field.remote_field.get_cache_name())
                    raise ValueError(
                        "save() prohibited to prevent data loss due to "
                        "unsaved related object '%s'." % field.name
                    )
        update_all()
