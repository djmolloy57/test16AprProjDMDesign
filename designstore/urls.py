from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.designstore, name="designstore"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('viewitem/', views.viewitem, name="viewitem"),
	#path('formpage/', views.form_name_view, name="form_name"),
]