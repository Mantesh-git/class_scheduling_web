from django.shortcuts import render # type: ignore

# Create your views here.

def index(request):
    return render(request, 'webapp/index.html')
def register(request):
    return render(request, 'webapp/register.html')

