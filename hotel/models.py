from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extension = ['.jpg', '.png']
    if not ext.lower() in valid_extension:
        raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=False, blank=False, validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)


class Hotel(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/hotel_cover/', null=False, blank=False, validators=[validate_file_extension])
    star = models.IntegerField(default=0, blank=False)
    city = models.CharField(max_length=128, null=False, blank=False)
    price = models.IntegerField(default=0, blank=False)
    # content = RichTextField()
    # created_at = models.DateTimeField(default=datetime.now, blank=False)

