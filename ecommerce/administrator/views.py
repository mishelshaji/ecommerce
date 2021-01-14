from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from product.forms import CategoryForm
from product.models import Category

# Create your views here.
@login_required
def home(request):
    return render(request, 'administrator/home.html')


class CategoryCreateView(CreateView):
    model = Category
    template_name = "administrator/category/create.html"
    form_class = CategoryForm
    success_url = '/administrator'


class CategoryListView(ListView):
    model = Category
    template_name = "administrator/category/list.html"

