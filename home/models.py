from django.db import models
from django.core.exceptions import ValidationError
import os
from django.utils import timezone

# Create your models here.
# Table for storing the data from contact us page

#Custom validator for image
from django.db import models
from django.core.exceptions import ValidationError
import os

# Custom validator for image file extensions
def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # Extract the file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are: .jpg, .jpeg, .png, .webp, .svg')


class Home(models.Model):
    heading = models.CharField(max_length=200)
    span = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='home/', validators=[validate_image_extension])
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.heading


class Website(models.Model):
    url = models.URLField(max_length=200)
    image = models.FileField(upload_to='websites/', validators=[validate_image_extension])  # FileField to support SVG
    title = models.CharField(max_length=200)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    projectImage = models.FileField(upload_to='websites/', validators=[validate_image_extension])  # FileField to support SVG
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class About(models.Model):
    heading = models.CharField(max_length=200)
    desc = models.TextField()
    t_project = models.CharField(max_length=50)
    t_country = models.CharField(max_length=50)
    o_project = models.CharField(max_length=50)
    view = models.CharField(max_length=50)
    image = models.FileField(upload_to='about/', validators=[validate_image_extension])

    def __str__(self):
        return self.heading


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to='projects/', validators=[validate_image_extension])
    url = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
class Team(models.Model):
    e_name = models.CharField(max_length=50)
    e_position = models.CharField(max_length=50)
    e_designation = models.CharField(max_length=50)
    e_image = models.FileField(upload_to='teams/', validators=[validate_image_extension])
    e_facebook = models.URLField(max_length=200)
    e_instagram = models.URLField(max_length=200)
    e_linkedin = models.URLField(max_length=200)
    e_github = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.e_name + 'Profile saved!'

class Review(models.Model):
    customername = models.CharField(max_length=50)
    customerdesignation = models.CharField(max_length=50)
    customerimage = models.FileField(upload_to='rcustomer/', validators=[validate_image_extension])
    customerreview = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'Review from ' + self.customername

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.first_name + ' - ' + self.email

