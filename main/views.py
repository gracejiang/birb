from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Chirp

# all views

# main (splash) page
def main_view(request):
    return render(request, 'main.html')

# home page
def home_view(request):
    # if not logged in, redirect to accounts page
    if not request.user.is_authenticated:
        return redirect('/accounts/')


    # if post request, insert into DB
    if request.method == 'POST' and request.POST['body'] != "":
        chirp = Chirp.objects.create(
            body = request.POST['body'],
            author = request.user
        )

    chirps = Chirp.objects.all()
    return render(request, 'home.html', {'chirps': chirps})

# delete a chirp routing
def delete_view(request):
    chirp = Chirp.objects.get(id=request.GET['id'])
    if chirp.author == request.user:
        chirp.delete()
    return redirect('/')

# accounts login/signup page
def accounts_view(request):
    return render(request, 'accounts.html', {})

# login a user
def login_view(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username = username, password = password)

    if user is not None:
        login(request, user)
        return redirect('/home/')
    else:
        return redirect('/accounts?error=True')

# register a user
def signup_view(request):
    user = User.objects.create_user(
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password']
    )

    login(request, user)
    return redirect('/home/')

# logout a user
def logout_view(request):
    logout(request)
    return redirect('/accounts/')

# profile page
def profile_view(request):
    chirps = Chirp.objects.filter(author=request.user)
    return render(request, 'profile.html', {'chirps': chirps})