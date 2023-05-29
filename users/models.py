from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

def __str__(self):
    return f'{self.user.username} Profile'


#to resize the image size we created our own save method. as img size tend to larger and willl eat up a lot space so we created this method. here we resizing image to 300*300 px. there are many ways to do that.
def save(self):
    super.save() #to run the save method of parent class. 

    img = Image.open(self.image.path) #it will open the img of current instance

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path) #to save it on the same path


#if we make any changes in model then we have to also do migration.