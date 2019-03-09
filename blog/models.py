from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    img_url = models.TextField(max_length=50000, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def has_comments(self):
        if (len(self.comment_set.objects.all()) > 0):
            return true
        else:
            return false

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + '-' + self.published_date