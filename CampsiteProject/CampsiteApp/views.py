from django.shortcuts import render
from .forms import BookingForm

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # You don't need to redirect, just render index.html again
            return render(request, 'index.html', {'form': form})
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})
