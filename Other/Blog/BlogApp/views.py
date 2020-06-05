from django.shortcuts import render
from django.http      import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.urls import reverse

# Create your views here.
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    ListView,
    DeleteView
)

from .models import Article
from .forms import ArticleForm

# def ArticleListView(request):
#     obj = Article.objects.all()
#     context = {
#         "obj" : obj
#     }
#     return render(request, "article_list.html", context)
class ArticleListView(ListView):
    template_name="article_list.html"
    queryset = Article.objects.all()

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name="article-create.html"
    queryset = Article.objects.all()

    def create_view(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def DetailView(request, id):
    obj = Article.objects.get(id=id)
    context = {
        "obj" : obj
    }
    return render(request, "article_detail.html", context)

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name="article-create.html"
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    # def create_view(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name="article_delete.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("Article-list")