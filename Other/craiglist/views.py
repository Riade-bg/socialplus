from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .forms import SearchForm
from requests.compat import quote_plus

# Create your views here.
BASE_URL = "https://newyork.craigslist.org/search/bbb?query=python%20tutor&sort=rel"
def index(request):
    return render(request, "base.html", {})

def new_search(request):
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    # search = form.cleaned_data['Search']
    # final_url = BASE_URL.format(quote_plus(search))
    response = requests.get(BASE_URL)
    contex = {
        # 'search': search
    }
    return render(request, "index.html", contex)