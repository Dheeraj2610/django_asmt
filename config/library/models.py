from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(
        max_length=100
    )
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=200, unique=True, null=False
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    summary = models.TextField()
    publish_date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.title
