from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("data published")

    def __str(self):
        return self.body