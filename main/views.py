from django.shortcuts import render
from main.models import Chirp

# all views
def main_view(request):
    chirps = Chirp.objects.all()
    return render(request, 'main.html', {'chirps': chirps})