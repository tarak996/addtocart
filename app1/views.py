from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .models import *


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['myname']='tarak'
        context['product_list']= Product.objects.all()
        return context


class AddToCartView(TemplateView):
    template_name ='addtocart.html'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        product_id=self.kwargs['pro_id']
        product_obj=Product.objects.get(id=product_id)

        cart_id=self.request.session.get('cart_id',None)
        if cart_id:
            cart_obj=Cart.objects.get(id=cart_id)
            this_product_in_cart=cart_obj.cartproduct_set.filter(product=product_obj)
            if this_product_in_cart.exists():
                cartproduct=this_product_in_cart.last()
                cartproduct.quantity+=1
                cartproduct.subtotal+=product_obj.selling_price
                cartproduct.save()
                cart_obj.total+=product_obj.selling_price
                cart_obj.save()
            else:
                cartproduct=CartProduct.objects.create(
                    cart=cart_obj,product=product_obj,rate=product_obj.selling_price,quantity=1,subtotal=product_obj.selling_price
                )
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
        else:
            cart_obj=Cart.objects.create(total=0)
            self.request.session['cart_id']=cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1,
                subtotal=product_obj.selling_price
            )
            cart_obj.total += product_obj.selling_price
            cart_obj.save()

        return context


class MyCartView(TemplateView):
    template_name = 'mycart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cart_id=self.request.session.get('cart_id',None)
        if cart_id:
            cart=Cart.objects.get(id=cart_id)
        else:
            cart=None
        context['cart']=cart
        return context


# class ManageCartView(TemplateView):
#
#     def get(self,r**kwargs):
#         context = super().get_context_data(**kwargs)
#         cart_id=self.kwargs['cp_id']
#         action=request.GET.get['action']
#         if action=='inc':
#             pass
#         elif action =='dcr':
#             pass
#         elif action =='rmv':
#             pass
#         return redirect('mycart')

class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'