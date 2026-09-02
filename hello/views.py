from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Nossa primeira aplicação Django.</h1>")