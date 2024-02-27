from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #User is different Table, first import 
                                            #Post Model, User Model have 1 to Many Relationship
from django.urls import reverse
from djrichtextfield.models import RichTextField
import random
class Post(models.Model): #inherite from models.Model class
    title = models.CharField(max_length = 100)
    excerpt = models.CharField(max_length = 300)
    
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    ingredients = RichTextField(max_length = 500, null = False, blank = True)
    content = RichTextField(max_length = 8000, null = False, blank = True)  #instructions
    image = models.ImageField('default.jpg', upload_to = 'recipe_pics', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {"pk": self.pk})


class RecipeBook(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Post, related_name='recipe_books')
    color = models.CharField(max_length=11, blank=True, null=True)  # RGB format, e.g., '255,0,0'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipebook-detail', kwargs={'pk': self.pk})

    def get_random_color(self):
        return f'{random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)}'

    def save(self, *args, **kwargs):
        # Generate a random color only if the color is not set
        if not self.color:
            self.color = self.get_random_color()
            print("Generated Color:", self.color)  # Add this line for debugging
        super().save(*args, **kwargs)
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set a default user ID here
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Set the name field to the username of the user who created the comment
        self.name = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.post.title} - {self.user.username}"