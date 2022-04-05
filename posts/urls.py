from django.urls import path

from posts import views

urlpatterns = [
    path('posts/', views.PostView.as_view(), name='posts-view'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts-update/<int:pk>/', views.PostDetailView.as_view()),
    path('posts-delete/<int:pk>/', views.PostDeleteView.as_view()),


]