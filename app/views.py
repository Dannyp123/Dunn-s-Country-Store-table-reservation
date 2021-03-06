from django.shortcuts import render
import random
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render
from app.data import BREAKFAST
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Create your views here
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
            email = form.cleaned_data["email"]

            models.TableReservation.submit_reservation(
                f_name, l_name, p_number, num_of_people, date, time, email)

            messages.success(
                request,
                f"Thank you for reserving a table!  We will email you when your table is ready."
            )

            return redirect("home")

        else:
            return render(request, "reservation-form.html",
                          {"reservation_form": form})


class TableReservation(View):
    def get(self, request):
        return render(request, "reservation-form.html",
                      {"reserve": models.TableReservation.objects.all()})


class ReservedTables(View):
    def get(self, request):
        return render(request, "reservered-tables.html",
                      {"reserved": models.TableReservation.objects.all()})


class ReservedTable(View):
    def get(self, request, id):
        return render(
            request, "reserved-table.html",
            {"reserved_table": models.TableReservation.objects.get(id=id)})


class Email(View):
    def get(self, request, id):
        random_num = random.randint(1, 9)

        reservation = models.TableReservation.objects.get(id=id)
        message = Mail(
            from_email=request.user.email,
            to_emails=reservation.email,
            subject="Table Confirmation - Dunn's Country Store",
            html_content=
            'The table you reserved is ready. Your table number is: {}. Just have a seat and someone will be right with you. <strong>* Make sure you arrive before 7:15 CST.*</strong>'
            .format(random_num))
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print(reservation.email)
        messages.success(request,
                         f"An email has been sent to {reservation.email}.")
        return redirect("reserved")


class Home(View):
    def get(self, request):
        return render(request, "home.html",
                      {"user_admin": models.TableReservation.objects.all()})


class DeleteReservation(View):
    def get(self, request, id):
        models.TableReservation.objects.get(id=id).delete()
        return redirect("reserved")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You can now login")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html",
                  {"profile": models.TableReservation.objects.all()})
