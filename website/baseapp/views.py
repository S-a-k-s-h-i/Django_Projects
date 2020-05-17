from django.db.models import Q
from django.shortcuts import render,redirect
from .models import Book_Product
from django.contrib import messages


# Create your views here.
def index(request):
         if request.method=='POST':
             Search=request.POST['Search']
             if Search:
                 match=Book_Product.objects.filter(Q(name__icontains=Search) | Q(author_name__icontains=Search))
                 if match:
                     context={'match':match}
                     return render(request,'index.html',context)
                 else:
                     messages.info(request,Search)
                     return redirect('index')
             else:
                 return redirect('index')
         else:
                books=Book_Product.objects.filter(offer=True)
                context={"books":books}
                return render(request,'index.html',context)

def product_details(request,pk):
       product=Book_Product.objects.get(pk=pk)
       context={
           'product':product
       }
       return render(request,'product_details.html',context)

def All_books(request):
    books=Book_Product.objects.all()
    context={
        'books':books
          }
    return render(request,'book_category.html',context)

# def book_category(request,sub_category):
#     category_books=Book_Product.objects.filter(sub_category__contains=sub_category)
#     context={
#         'category_books':category_books
#     }
#     return render(request,'book_category.html',context)