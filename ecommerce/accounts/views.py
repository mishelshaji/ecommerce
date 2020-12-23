from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerDetails

# Create your views here.
def user_authenticate(request):
    if request.method == "GET":
        context = {}
        context['form'] = AuthenticationForm()
        context['detailsform'] = AuthenticationForm()
        return render(request, 'accounts/authenticate.html', {'form': AuthenticationForm()})
    
    