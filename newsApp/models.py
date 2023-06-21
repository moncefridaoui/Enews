from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title
