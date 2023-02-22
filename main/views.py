from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

from .forms import ContactForm, LoginForm, RegisterForm

User = get_user_model()


def homepage(req):
    return render(req, "main/index.html", context={"x": "azxc"})


def about_page(req):
    return render(req, "about.html")


def contact_page(req):
    context = {}
    form = ContactForm(req.POST or None)
    context["form"] = form
    if req.method == "POST":
        if form.is_valid:
            pass
    return render(req, "contact.html", context)


def login_page(req):
    ctx = {}
    form = LoginForm(req.POST or None)
    if not req.method == "POST" or not form.is_valid():
        ctx["form"] = form
        return render(req, "login.html", ctx)

    user = authenticate(req, username=form.username, password=form.password)
    if not user:
        raise
    login(req, user)
    return redirect("")


def register_page(req):
    form = RegisterForm()
    context = {"form": form}

    if form.is_valid():
        username = form.changed_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create(
            username=username, password=password, email=email
        )
