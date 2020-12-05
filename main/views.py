from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Chirp, Hashtag
from datetime import datetime

# all views

# home page – both splash and home page depending on if user is logged 
# in or not
def main_view(request):
    # if not logged in, redirect to accounts page
    # if not request.user.is_authenticated:
    #     return redirect('/accounts/')

    # if post request, insert into DB
    if request.method == 'POST' and request.POST['body'] != "":
        tags = get_hashtags(request.POST['body'])
        chirp = Chirp.objects.create(
            body = request.POST['body'],
            author = request.user,
            created_at = datetime.now()
        )
        for tag in tags:
            hashtag = get_hashtag(tag)
            hashtag.save()
            chirp.hashtags.add(hashtag)
            chirp.save()

    chirps = Chirp.objects.all().order_by('-created_at')
    return render(request, 'main.html', {'chirps': chirps})

# delete a chirp routing
def delete_view(request):
    chirp = Chirp.objects.get(id=request.GET['id'])
    if chirp.author == request.user:
        chirp.delete()
    return redirect('/')

# delete a chirp routing from profile
def delete_view_from_profile(request):
    chirp = Chirp.objects.get(id=request.GET['id'])
    if chirp.author == request.user:
        chirp.delete()
    return redirect('/profile/')

# accounts login/signup page
def accounts_view(request):
    return render(request, 'accounts.html', {})

# login a user
def login_view(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username = username, password = password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/?error=True')

# register a user
def signup_view(request):
    if request.POST['username'] is not "" and request.POST['email'] is not ""\
        and request.POST['password'] is not "":
        user = User.objects.create_user(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password']
        )

        login(request, user)
    return redirect('/')

# logout a user
def logout_view(request):
    logout(request)
    return redirect('/')

# user page
def user_view(request, username):
    user = User.objects.get(username=username)
    chirps = Chirp.objects.filter(author=user).order_by('-created_at')
    return render(request, 'user.html', {'user': user, 'chirps': chirps})

def splash_view(request):
    return render(request, 'splash.html')

def hashtag_view(request, tag):
    hashtag = get_hashtag(tag)
    chirps = Chirp.objects.filter(hashtags__tag=hashtag).order_by('-created_at')
    return render(request, 'hashtag.html', {'hashtag': hashtag, 'chirps': chirps})

# like a chirp
def like_chirp(request):
    chirp = Chirp.objects.get(id=request.GET['id'])
    print(chirp.body, chirp.likes.all)
    chirp.likes.add(request.user)
    chirp.save()
    print(chirp.likes)
    return redirect('/')

def get_hashtags(text):
    hashtags = []
    hashtag_index = text.find("#")
    while hashtag_index >= 0:
        text = text[hashtag_index:]
        whitespace_index = text.find(" ")
        if whitespace_index > 0:
            tag = text[1:whitespace_index]
            hashtags.append(tag)
            text = text[whitespace_index:]
        else:
            tag = text[1:]
            hashtags.append(tag)
            text = ""
        hashtag_index = text.find("#")
    return hashtags

def get_hashtag(tag):
    try:
        hashtag = Hashtag.objects.get(tag=tag)
    except Hashtag.DoesNotExist:
        hashtag = Hashtag.objects.create(tag=tag)
    print(hashtag)
    return hashtag