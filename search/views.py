from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("search form and results will go here.")