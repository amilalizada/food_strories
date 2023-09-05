from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib import messages
from core.forms import ContactForm
from .models import Contact
# Create your views here.


def home(request):

    text = "Hi! My name is Cathy Deon, behind the word mountains. far from the countries Vokalia and Consonantia. there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
    context = {
        "text": text
    }
    
    return render(request, "index.html", context=context)


def contact(request):
    form = ContactForm()
    
    if request.method == "POST":
        post_data = request.POST
        form = ContactForm(data=post_data)
        if form.is_valid():
            form.save()
    context = {
        "form": form
    }
    return render(request, "contact.html", context=context)


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("core:contact")

    def get_success_url(self) -> str:
        messages.success(self.request, "Contact is sent")

        return super().get_success_url()
