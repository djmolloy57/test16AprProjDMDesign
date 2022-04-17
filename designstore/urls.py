from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.designstore, name="designstore"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('viewitem/', views.viewitem, name="viewitem"),
	#path('formpage/', views.form_name_view, name="form_name"),
	path('add', views.add_item, name="add"),
	path('edit/<item_id>', views.edit_item, name="edit"),
	path('toggle/<item_id>', views.toggle_item, name="toggle"),
	path('delete/<item_id>', views.delete_item, name="delete"),
]

