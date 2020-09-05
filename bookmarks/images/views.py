from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

# Create your views here.

@login_required
def image_create(request):
    if request.method == "POST":
        #Formularz został wysłany
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            #Dane formularza są prawidlowe
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #Przypisanie biezacego uzytkownika do elementu
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Obraz zostal dodany.')
            #Przekierowanie do widoku szczegolowego dla nowo utworzonego elementu
            return redirect(new_item.get_absolute_url())
    else:
        #utowrzenie formularza na podstawie danych dostarczonych przez bookmarket w żadaniu GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section':'images', 'form':form})
