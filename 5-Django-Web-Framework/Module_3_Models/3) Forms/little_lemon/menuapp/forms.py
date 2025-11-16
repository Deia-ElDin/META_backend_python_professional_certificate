from django import forms

SHIFTS = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
)

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, label='First Name', required=False)
    last_name = forms.CharField(max_length=200, label='Last Name', required=False)
    shift = forms.ChoiceField(choices=SHIFTS, label='Shift')
    time_log = forms.TimeField()
   