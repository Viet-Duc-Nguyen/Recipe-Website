from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, RecipeBook, Comment #Post is Recipe
from .forms import PostForm, UpdatePostForm, RecipeBookForm, CommentForm
from django.contrib import messages

from django.urls import reverse, reverse_lazy


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context) #connecting template/html with context(data)



class PostListView(ListView):
    model = Post
     #looking for <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts' #attribute is used to define the variable name that will be used in the template
    ordering = ['-date_posted'] #newest to oldest


class PostDetailView(DetailView):
    model = Post
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
class PostCreateView(LoginRequiredMixin, CreateView): # can only create post when logged in
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html' 
    


    
    
    def form_valid(self, form):
        form.instance.author = self.request.user #Recipe author will be logged in user

        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Print statements for debugging
        print("Form is valid")
        print("Form data:", form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Print statements for debugging
        print("Form is invalid")
        print("Form errors:", form.errors)
        return super().form_invalid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
######### Recipe Book views

class RecipeBookListView(ListView):
    model = RecipeBook
    template_name = 'blog/recipebook_list.html'
    context_object_name = 'recipe_books'
    ordering = ['-date_created']

class RecipeBookDetailView(DetailView):
    model = RecipeBook
    template_name = 'blog/recipebook_detail.html'
    context_object_name = 'recipe_book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        
        book_id = self.kwargs["pk"]
        context['recipebook_id'] = book_id
        book = RecipeBook.objects.get(id=book_id)
        book_recipes = book.recipes.all()
        print(book_recipes)
        context['book_recipes'] = book_recipes
        
        return context
    
@method_decorator(login_required, name='dispatch')
class RecipeBookCreateView(LoginRequiredMixin, CreateView):
    model = RecipeBook
    form_class = RecipeBookForm
    template_name = 'blog/recipebook_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.color = form.instance.get_random_color()  # Assign random color
        print("Random Color:", form.instance.color)  # Add this line for debugging
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the user's profile page after creating the recipe book
        return '/profile/'
@method_decorator(login_required, name='dispatch')
class RecipeBookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RecipeBook
    form_class = RecipeBookForm
    template_name = 'blog/recipebook_form.html'

    def test_func(self):
        recipe_book = self.get_object()
        return self.request.user == recipe_book.author

@method_decorator(login_required, name='dispatch')
class RecipeBookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = RecipeBook
    success_url = '/'

    def test_func(self):
        recipe_book = self.get_object()
        return self.request.user == recipe_book.author
    
class AddRecipeToBookView(View):
    def post(self, request, recipebook_id, recipe_id):
        book = get_object_or_404(RecipeBook,id=recipebook_id)
        recipe  = get_object_or_404(Post, id = recipe_id)
        
        book.recipes.add(recipe) 
        return redirect(reverse('recipebook-detail', kwargs = {"pk": recipebook_id}))
    
class DeleteRecipeFromBookView(View):
    def get(self, request, recipebook_id, recipe_id):
        # Retrieve the recipe book and recipe objects
        book = get_object_or_404(RecipeBook, id=recipebook_id)
        recipe = get_object_or_404(Post, id=recipe_id)

        # Remove the recipe from the recipe book
        book.recipes.remove(recipe)

        # Redirect to the recipe book detail view
        return redirect(reverse('recipebook-detail', kwargs={"pk": recipebook_id}))


# Add delete recipe from book
def add_recipe_to_recipebook(request, recipebook_id, recipe_id):
    recipebook = get_object_or_404(RecipeBook, id=recipebook_id)
    recipe = get_object_or_404(Post, id=recipe_id)

    if recipe not in recipebook.recipes.all():
        recipebook.recipes.add(recipe)
        messages.success(request, f"Recipe '{recipe.title}' added to '{recipebook.title}'.")
    else:
        messages.warning(request, f"Recipe '{recipe.title}' is already in '{recipebook.title}'.")

    return redirect('recipebook-detail', pk=recipebook.id)

def remove_recipe_from_recipebook(request, recipebook_id, recipe_id):
    recipebook = get_object_or_404(RecipeBook, pk=recipebook_id)
    recipe = get_object_or_404(Post, pk=recipe_id)

    if request.user == recipebook.author:
        recipebook.recipes.remove(recipe)
        messages.success(request, f'Recipe "{recipe.title}" removed from "{recipebook.title}"')
    else:
        messages.error(request, 'You do not have permission to remove this recipe from the recipe book.')

    return redirect('recipebook-detail', pk=recipebook_id)


#Comment
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # Update with the correct path
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the current page (comment_form.html) after successful form submission
        return self.request.path
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['comments'] = context['post'].comments.all()
        return context