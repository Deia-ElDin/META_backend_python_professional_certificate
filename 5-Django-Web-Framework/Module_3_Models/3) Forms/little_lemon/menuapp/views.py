from django.shortcuts import render

# Create your views here.

from .forms import InputForm

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)