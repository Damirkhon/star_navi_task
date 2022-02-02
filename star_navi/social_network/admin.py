from django.contrib import admin

from .models import Post, PostLikes, Profile

admin.site.register(Post)
admin.site.register(PostLikes)
admin.site.register(Profile)