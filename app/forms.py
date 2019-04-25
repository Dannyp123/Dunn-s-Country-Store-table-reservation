from django import forms


class TableReservationForm(forms.Form):
    f_name = forms.CharField()
    l_name = forms.CharField()
    p_number = forms.RegexField(
        regex=
        r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
    )
    num_of_people = forms.IntegerField()
    date = forms.DateField()
    time = forms.TimeField()
    email = forms.EmailField()