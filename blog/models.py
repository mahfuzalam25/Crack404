from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)
    password = models.CharField(max_length=128, default=make_password('defaultpassword'))  # Hashed password storage

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.FileField(upload_to='blogimg/', blank=True, null=True)

    def __str__(self):
        return self.title
