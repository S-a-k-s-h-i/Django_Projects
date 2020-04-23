from django.urls import path
from . import views
urlpatterns=[
    path('',views.index.as_view(),name='index'),
    path('product_detail/<int:pk>',views.product_details.as_view(),name='product_detail'),
]