from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # we are passing arguent in datetimefield. here if we use 'auto_now' means whenever author make an edit the time of the post will be updated.
    # if we use 'auto_now_add' then it will remember the time when the post was posted.
    # we are using default with timezone variation. idk why but video used it
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    #here user can have multiple post but one post can only have one user. if user deletes his profile then the on_delete comes to play. we are passing models.CASCADE that means we are telling it to delete the post as well. this user works as key.

