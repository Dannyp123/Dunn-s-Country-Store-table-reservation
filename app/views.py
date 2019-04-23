from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render
from app.data import BREAKFAST


# Create your views here.
class HomePage(View):
    def get(self, request):
        return render(request, "home.html")


class HuntingFishing(View):
    def get(self, request):
        return render(request, "hunting-fishing.html")


class BeerTobacco(View):
    def get(self, request):
        return render(request, "beer-tobacco.html")


class Menu(View):
    def get(self, request):
        return render(request, "menu.html", {"BREAKFAST": BREAKFAST})


class MakeReservation(View):
    def get(self, request):
        return render(request, "reservation-form.html",
                      {"reservation_form": forms.TableReservationForm()})

    def post(self, request):
        form = forms.TableReservationForm(data=request.POST)
        if form.is_valid():
            f_name = form.cleaned_data["f_name"]
            l_name = form.cleaned_data["l_name"]
            p_number = form.cleaned_data["p_number"]
            num_of_people = form.cleaned_data["num_of_people"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]

            models.TableReservation.submit_reservation(
                f_name, l_name, p_number, num_of_people, date, time)

            return redirect("reservation")

        else:
            return render(request, "reservation-form.html",
                          {"reservation_form": form})


class TableReservation(View):
    def get(self, request):
        return render(request, "reservation-form.html",
                      {"reserve": models.TableReservation.objects.all()})
