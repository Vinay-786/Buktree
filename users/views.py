from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


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
