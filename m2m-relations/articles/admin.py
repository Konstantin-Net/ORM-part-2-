from django.contrib import admin

from .models import Article, Tag


class TagInline(admin.TabularInline):
    model = Tag.members.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]

