from django.shortcuts import render, HttpResponse
from django.template import loader
import json

import requests

# Create your views here.
def index(request):
    
    template = loader.get_template('index.html')

    return render(request, 'index.html', {'btc': 'aaa'})


def api(request):
    btc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd,eur,pln")
    
    return HttpResponse(json.dumps(btc_price.json()), content_type="application/json")