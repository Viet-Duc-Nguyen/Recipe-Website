from django.contrib import admin
from .models import Post, RecipeBook, Comment
# Register your models here.


admin.site.register(Post)
admin.site.register(RecipeBook)
admin.site.register(Comment)

