from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='categories', default=None, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='authors', default=None, null=True)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

class Article(models.Model):
    title = models.CharField(max_length=200)
    perex = models.TextField()
    text = models.TextField()
    published = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    categories = models.ManyToManyField(Category, related_name='articles')
    vote_sum = models.IntegerField(default=0)
    vote_count = models.IntegerField(default=0)

    def vote_avg(self):
        return self.vote_sum / self.vote_count if self.vote_count > 0 else 0        

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    time = models.DateTimeField(auto_now_add=True, null=True)
    ip = models.GenericIPAddressField(default=None, null=True)
    user_agent = models.CharField(max_length=200, default=None, null=True)
  
    def __str__(self):
        return str(self.name)


