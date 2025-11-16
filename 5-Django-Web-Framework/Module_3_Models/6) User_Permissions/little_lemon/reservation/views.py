from django.shortcuts import render

# Create your views here.

from .forms import ReservationForm


def reservation_view(request):
    form = ReservationForm()
    if (request.method == 'POST'):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form saved")
        else:
            print(form.errors)
        
    context = {"form": form}
    return render(request, "reservation.html", context)