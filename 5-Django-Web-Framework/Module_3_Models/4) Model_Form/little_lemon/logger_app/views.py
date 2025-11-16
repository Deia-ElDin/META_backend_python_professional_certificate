from django.shortcuts import render

# Create your views here.

from .form import LoggerForm


def logger_view(request):
    print("Logger view")
    form = LoggerForm()
    if request.method == 'POST':
        form = LoggerForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            form.save()
            print("Form saved")
        else:
            print("Form is not valid")
            print(form.errors)
    context = {"form": form}
    return render(request, "logger.html", context)