from django.db import models
from django.utils.text import slugify
# from ckeditor.fields import RichTextField
# from applymode.models import Apply


# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=200)


class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)


class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)


class JobPost(models.Model):
    JOBS_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    expire = models.DateField(null=True)
    salary = models.IntegerField()
    url = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)
    type = models.CharField(max_length=200, null=False, choices=JOBS_TYPE_CHOICES)

    # apply = models.ManyToManyField('applymode.ApplyForm', null=True, on_delete=models.CASCADE)

    # auth

    def save(self, *args, **kwargs):
        print(self.id)
        if not self.id:
            self.url = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} with {self.salary}"
