from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login/', views.logging, name='login'),
    path('logout',views.logout_view,name='logout'),
    path('detail',views.detail_view,name='detail'),
]
