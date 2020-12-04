from django.shortcuts import render, redirect
from main.models import Chirp

# all views


# home page
def main_view(request):
    # if post request, insert into DB
    if request.method == 'POST' and request.POST['body'] != "":
        chirp = Chirp.objects.create(
            body = request.POST['body']
        )

    chirps = Chirp.objects.all()
    return render(request, 'main.html', {'chirps': chirps})


# delete routing
def delete_view(request):
    # chirp = Chirps.objects.get(id=request.POST[], request=)
    chirp = Chirp.objects.get(id=request.GET['id'])
    chirp.delete()
    return redirect('/')