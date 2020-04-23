from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book_Product
# Create your views here.
class index(ListView):
    model=Book_Product
    template_name = 'index.html'



class product_details(DetailView):
       model = Book_Product
       template_name ='product_details.html'
       context_object_name = 'batman'
