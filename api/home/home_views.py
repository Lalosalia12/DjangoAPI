from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGING_URL



@login_required(login_url=LOGING_URL)
def home_views(request):
    template_name = "index.html"
    
    return render(request, template_name)

