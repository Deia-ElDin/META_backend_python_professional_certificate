from django.http import HttpResponse, HttpResponseNotFound



def home(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Page")

def handler404(request, exception):
    # return HttpResponse("Page not found")
    return HttpResponseNotFound("Page not found !")

