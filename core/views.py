from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

    text = "Hi! My name is Cathy Deon, behind the word mountains. far from the countries Vokalia and Consonantia. there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
    context = {
        "text": text
    }
    
    return render(request, "index.html", context=context)