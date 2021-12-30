from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):

    ordering = '-published_at'
    template = 'articles/news.html'
    article = Article.objects.all().order_by(ordering)
    scopes = Tag.objects.all()
    context = {'article': article,
               'scopes': scopes
               }

    return render(request, template, context)
