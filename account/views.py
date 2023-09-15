from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View
from .forms import LoginForm, RegisterForm
from stories.models import Recipe
from .tasks import send_mail_custom
from .utils import account_activation_token
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from django.contrib.auth import get_user_model
# Create your models here.
USER = get_user_model()


# Create your views here.

class CustomLoginView(LoginView):
    template_name = "login.html" 
    form_class = LoginForm


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("account:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = self.request.META['HTTP_HOST']
        send_mail_custom(user, current_site)

        return response
    

class ActivateView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get("uidb64")
        token = kwargs.get("token")
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = USER.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, USER.DoesNotExist):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            # user.profile.email_confirmed = True
            user.save()
            return redirect('account:login')
        else:
            return render(request, 'activation.html')
    

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect(reverse_lazy("account:login"))
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    
    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if user:
                django_login(request, user)
                return redirect(reverse_lazy("account:profile"))
    else: form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)


@login_required
def profile(request):
    
    return render(request, "user-profile.html")

@login_required
def logout(request):
    
    django_logout(request)
    return redirect(reverse_lazy("account:login"))   