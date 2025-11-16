from django.shortcuts import render
from .forms import MenuItemForm

def menu_view(request):
    form = MenuItemForm()
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid(): 
            form.save()
        else:
            print(form.errors)
    context = {"form": form}
    return render(request, "menu.html", context)
