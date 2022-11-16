
from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('add-to-cart-<int:pro_id>/',AddToCartView.as_view(),name='addtocart'),
    path('mycart/',MyCartView.as_view(),name='mycart'),
    #path('manage-cart/<int:cp_id>/',ManageCartView.as_view(),name='managecart')
]