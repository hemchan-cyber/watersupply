from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def client(request):
    return render(request, 'client.html')

def reservoir(request):
    return render(request, 'reservoir.html')