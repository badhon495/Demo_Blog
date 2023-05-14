from django.urls import path
from . import views  # dot diye same dirctory theke views file ta import kortesi


urlpatterns = [
    path('', views.home, name = 'blog-home'),
    #first parameter empty karon home page ke indicate kortese.
    #second parameter e views.home ke deoa hoyeche. kron eita oikahne niye jabae. httpsresponse return kore
    #third parameter hocche name for the path
    
    path('about/', views.about, name = 'blog-about')
]
