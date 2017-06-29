from django.db import models
from django.urls import reverse
# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    headshot = models.ImageField(upload_to='author_headshots', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author', kwargs={'pk': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    def display_authors(self):
        return ','.join([obj.name for obj in self.authors.all()])

    display_authors.short_description = 'authors'







