from django import forms
from .models import BookingRecord

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRecord
        fields = ['name', 'email', 'arrival_Date', 'depature_Date', 'guests']
