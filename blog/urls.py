from django.urls import path,include
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    RecipeBookListView, RecipeBookDetailView, RecipeBookCreateView,RecipeBookUpdateView, RecipeBookDeleteView,
    add_recipe_to_recipebook, remove_recipe_from_recipebook,
    CommentCreateView
)
from users.views import profile as user_profile
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #url for POSTS
    path('', PostListView.as_view(), name = 'blog-home'), #looking for <app>/<model>_<viewtype>.html
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('about/', views.about, name = 'blog-about'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    #url for Recipe Books
    path('recipebook/', RecipeBookListView.as_view(), name='recipebook-list'),
    path('recipebook/<int:pk>/', RecipeBookDetailView.as_view(), name='recipebook-detail'),
    path('recipebook/new/', RecipeBookCreateView.as_view(), name='recipebook-create'),
    path('recipebook/<int:pk>/update/', RecipeBookUpdateView.as_view(), name='recipebook-update'),
    path('recipebook/<int:pk>/delete/', RecipeBookDeleteView.as_view(), name='recipebook-delete'),
    
    # add, delete recipe from book 
    path('recipebook/<int:recipebook_id>/add-recipe/<int:recipe_id>/', add_recipe_to_recipebook, name='add-recipe-to-recipebook'),
path('recipebook/<int:recipebook_id>/remove-recipe/<int:recipe_id>/', remove_recipe_from_recipebook, name='remove-recipe-from-recipebook'), 
    
    #comment
     path("posts/comment/<int:pk>/", CommentCreateView.as_view(), name="add_comment"),
     
     path('profile/<str:username>/', user_profile, name='user_profile')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
