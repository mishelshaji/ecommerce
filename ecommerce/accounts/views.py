from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def user_authenticate(request):
    return render(request, 'accounts/authenticate.html')