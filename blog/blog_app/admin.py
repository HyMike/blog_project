from django.contrib import admin
from .models import Post, Author, Tag, CommentsModel

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'date', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('userName', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(CommentsModel, CommentAdmin)
