from django import forms


class TableReservationForm(forms.Form):
    f_name = forms.CharField()
    l_name = forms.CharField()
    p_number = forms.RegexField(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    num_of_people = forms.IntegerField()
    date = forms.DateField()
    time = forms.TimeField()
    email = forms.EmailField()