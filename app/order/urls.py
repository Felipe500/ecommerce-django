from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('pay-order/', views.PayOrderView.as_view(), name="pay_order"),
    path('detail-order/', views.DetailOrderView.as_view(), name="detail_order"),
    path('save-order/', views.SaveOrder.as_view(), name="save_order"),
]
