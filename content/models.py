from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

class Article(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    text = models.TextField()
    published = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    categories = models.ManyToManyField(Category, related_name='articles')

    def __str__(self):
        return str(self.title)



