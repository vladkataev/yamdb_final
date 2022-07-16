from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Review, Title, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'score', 'author', 'title_id')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'author', 'text')


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(GenreTitle)
admin.site.register(Review)
admin.site.register(Comment)
