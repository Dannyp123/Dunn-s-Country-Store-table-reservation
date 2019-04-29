from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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


class UserResisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if len(user.username) > 10:
            user.is_staff = True
            user.save()
        else:
            user.is_staff = False
        return user
