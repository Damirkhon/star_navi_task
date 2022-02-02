from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    likes = models.ManyToManyField(User, through='PostLikes',related_name="likedPosts")

    def likePost(self, user):
        self.likes.add(user)
        self.save()
    
    def unlikePost(self, user):
        self.likes.remove(user)
        self.save()

class PostLikes(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.DateField(null=True, blank=True, auto_now_add=True)
    count = models.IntegerField(blank=True, default=1)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField()