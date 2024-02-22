from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
# from .forms import ReviewForm
from .models import Post, ReviewRating
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    context = Post.objects.all()
    return render(request, 'movie/home.html', {'posts': context})


class PostListView(ListView):
    model = Post
    template_name = 'movie/home.html'
    context_object_name = 'posts'
    ordering = ['-release_date']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['movie_image','movie_name', 'movie_description', 'release_date', 'actors', 'youtube']
    success_url = '/'
    def form_valid(self, form):
        form.instance.movie_user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['movie_image','movie_name', 'movie_description', 'release_date', 'actors', 'youtube']

    def form_valid(self, form):
        form.instance.movie_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.movie_user:
            return True
        return False


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.movie_user:
            return True
        return False


class ReviewRatings(CreateView):
    model = ReviewRating
    fields = ['review', 'rating']
    success_url = '/'

    def form_valid(self, form):
        form.instance.review_user = self.request.user
        form.save()
        return super().form_valid(form)


class ReviewListView(ListView):
    model = ReviewRating
    template_name = 'movie/review_display.html'
    context_object_name = 'posts'

def SearchResult(request):
 movies=None
 query=None
 if 'q' in request.GET:
    query1=request.GET.get('q')
    query=query1.upper()
    if query.isalnum():
        movies=Post.objects.all().filter(Q(movie_name__contains=query) | Q(movie_description__contains=query))
    return render(request,'movie/search.html',{'query':query,'movie':movies})

