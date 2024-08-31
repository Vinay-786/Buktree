from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UpdateProfile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
        print("form is not valid")
    return render(request, 'registration/signup.html', {'form': form})


def logoutpage(request):
    return render(request, 'logoutpage.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES,
                             instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfile(instance=request.user)

    return render(request, "users/updateprofile.html", {"form": form})
