from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerDetailsForm, RegistrationForm
from django.db import transaction
from django.contrib import messages

# Create your views here.
def user_authenticate(request):
    if request.method == "GET":
        context = {}
        context['form'] = RegistrationForm()
        context['detailsform'] = CustomerDetailsForm()
        context['loginform'] = AuthenticationForm()
        return render(request, 'accounts/authenticate.html', context)

@transaction.atomic 
def register(request):
    rf = RegistrationForm(request.POST)
    df = CustomerDetailsForm(request.POST)
    if rf.is_valid() and df.is_valid():
        user = rf.save(commit=False)
        user.set_password(rf.cleaned_data.get('password'))
        user.save()

        customer = df.save(commit=False)
        customer.user = user
        customer.save()
        messages.success(request, "Account created. You can now login.")
        return redirect('accounts_login')
    print(rf.errors)
    print(df.errors)
    context = {}
    context['form'] = rf
    context['detailsform'] = df
    context['loginform'] = AuthenticationForm()
    return render(request, 'accounts/authenticate.html', context)