from django.urls import path
# from .views import PostListView
from . import views  # dot diye same dirctory theke views file ta import kortesi


urlpatterns = [
    path('', views.PostListView.as_view(), name = 'blog-home'),
    #first parameter empty karon home page ke indicate kortese.
    #second parameter e views.home ke deoa hoyeche. kron eita oikahne niye jabae. httpsresponse return kore
    #third parameter hocche name for the path
    
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'), #pk  means primary key. post/<int:pk> means it will got to post/primary key. here primary key post id.
    path('post/new/', views.PostCreateView.as_view(), name = 'post-create'), #nameofthemodel_form for this it will be post_form
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post-delete') #post_confirm_delete.html
]
