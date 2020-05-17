from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('<int:pk>',views.product_details,name='product_detail'),
    path('allbooks/',views.All_books,name='all_books'),
    # path('<category>/',views.book_category,name='book_category')
]