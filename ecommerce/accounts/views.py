from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerDetailsForm, RegistrationForm
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_authenticate(request):
    if request.method == "GET":
        context = {}
        context['form'] = RegistrationForm()
        context['detailsform'] = CustomerDetailsForm()
        context['loginform'] = AuthenticationForm()
        return render(request, 'accounts/authenticate.html', context)
    elif request.method == "POST":
        lf = AuthenticationForm(data=request.POST)
        if lf.is_valid():
            username = lf.cleaned_data.get('username')
            password = lf.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user.is_admin:
                return redirect('admin_home')
            elif user.is_customer:
                return redirect('customer_home')
        
        # If the form is not valid
        context = {}
        context['form'] = RegistrationForm()
        context['detailsform'] = CustomerDetailsForm()
        context['loginform'] = lf
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