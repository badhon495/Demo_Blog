from django.contrib import admin
from .models import Post
#here we can resgister our model. by registering the model the blog post will show up on admin page.

admin.site.register(Post)