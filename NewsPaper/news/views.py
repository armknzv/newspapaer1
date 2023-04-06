from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class Posts(ListView):
    model = Post
    template_name = 'posts_search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-date_time_in')
    paginate_by = 2

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        qs = self.get_filter().qs
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = self.get_filter()
        context['filter'] = filter
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'post'


class PostCreateViews(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    template_name = 'news/post_create.html'
    form_class = PostForm


class PostDeleteViews(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'news.delete_post'
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


class PostUpdateViews(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'news.change_post'
    template_name = 'news/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)