from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ListProductView.as_view(), name="list"),
    path('<slug>', views.DetailsProductView.as_view(), name="detail"),
    path('add-to-car/', views.AddToCarProductView.as_view(), name="add_to_car"),
    path('remove-to-car/', views.RemoveToCarProductView.as_view(), name="remove_to_car"),
    path('shopping-cart/', views.ShoppingCartView.as_view(), name="shopping_car"),
    path('shopping-summary/', views.ShoppingSummaryView.as_view(), name="shopping_summary"),
    path('finish-shopping-cart/', views.FinishShoppingCartView.as_view(), name="finish_shopping_cart"),
]
