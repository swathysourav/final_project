
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ReviewRatings,ReviewListView

urlpatterns = [
    path('',PostListView.as_view(),name='movie-home'),
     path('review/',ReviewListView.as_view(),name='post-review'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/rating',ReviewRatings.as_view(),name='post-review'),
     path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('search/',views.SearchResult,name='post-search'),

]
