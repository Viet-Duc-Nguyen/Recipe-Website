from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

def profile(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        # Rest of your view logic
        return render(request, 'users/profile.html', {'user': user})
    else:
        # Handle the case where 'username' is not provided, for example, redirect to home page
        return redirect('blog-home')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a profile for the user if it doesn't exist
            profile, created = Profile.objects.get_or_create(user=user)

            if created:
                messages.success(request, f'Account and profile created for {user.username}!')
            else:
                messages.info(request, f'Account created for {user.username}. Profile already exists.')

            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)