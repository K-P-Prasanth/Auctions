from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Category,create_listing,Owner


def index(request):
    return render(request, "auctions/index.html",{
            "items" : create_listing.objects.all(),
            "msg" : "No Items at Auction"
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        st_bid = request.POST["st_bid"]
        image = request.POST["image"]
        category = Category.objects.get(pk=request.POST["category"])
        username = request.POST["username"]


        # passenger = create_listing.objects.get(pk=int(request.POST["passenger"]))
        # passenger.flights.add(flight)


        f = create_listing(title=title,description=description,st_bid=st_bid,image=image,category=category,owner=username,max_bidder = username)
        f.save()



        items = create_listing.objects.all()

        return render(request, "auctions/index.html",{
            "items" : items,
            "msg" : "No Items at Auction",
            "owner" : username
        })
    else:
        categories = Category.objects.all()
        return render(request,"auctions/create.html",{
            "categories":categories
        })
    

def view(request,item_id):
    if request.method == "POST":
        item = request.POST["item"]
        st_bid = request.POST["amount"]
        bidder = request.POST["bidder"]
        create_listing.objects.filter(pk=item_id).update(st_bid=st_bid,max_bidder=bidder)
        item = create_listing.objects.get(pk=item_id)
        return render(request,"auctions/view.html",{
            "item" : item
        })
    else:
        item = create_listing.objects.get(pk=item_id)

        return render(request,"auctions/view.html",{
            "item" : item
        })
