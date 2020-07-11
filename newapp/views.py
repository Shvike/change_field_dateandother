from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from newapp.models import Author, Blog, Entry
from datetime import date


def main_page(request):
    return render(request, "index.html", {"name":"Bogdan"})


class main_view(View):

    def get(self, request):
        response = {}
        response['entryes'] = Entry.objects.all()
        response['name'] = "Bogdan"
        return render(request, "index.html", response)

    def post(self, request):
        username = request.POST.get("login")
        pwd = request.POST.get("password")
        if username is None:
            logout(request)
            return redirect("main")
        user = authenticate(username=username, password=pwd)
        if user is not None:
            login(request, user)
        return redirect("main")


class UpdateEntry(View):
    def post(self, request, id):
        hl = request.POST["headline"]
        Entry.objects.filter(id=id).update(headline=hl)
        # print(Entry.objects.get(id=id).pub_date)
        bl = request.POST["blog__name"]
        b = Entry.objects.filter(id=id)[0].blog
        b.name = bl
        b.save()

        bt = request.POST["body_text"]
        Entry.objects.filter(id=id).update(body_text=bt)

        y, m, d = request.POST["pub_date"].split("-")
        m = int(m.lstrip("0"))
        d = int(d.lstrip("0"))
        y = int(y)
        e = Entry.objects.get(id=id)
        e.pub_date = date(y, m, d)
        e.save()
        return redirect("main")
# Create your views here.
