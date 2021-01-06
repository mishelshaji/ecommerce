from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerDetailsForm, RegistrationForm

# Create your views here.
def user_authenticate(request):
    if request.method == "GET":
        context = {}
        context['form'] = RegistrationForm()
        context['detailsform'] = CustomerDetailsForm()
        context['loginform'] = AuthenticationForm()
        return render(request, 'accounts/authenticate.html', context)
    
    