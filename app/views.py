from django.shortcuts import render
from django.views import View
from app import forms
from app import models
from django.shortcuts import redirect, render


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
        return render(request, "menu.html")