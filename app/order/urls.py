from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('list/', views.ListOrderView.as_view(), name='list'),
    path('save-order/', views.SaveOrder.as_view(), name="save_order"),
    path('detail-order/<int:pk>', views.DetailOrderView.as_view(), name="detail_order"),
    path('pay-order/<int:pk>', views.PayOrderView.as_view(), name="pay_order"),

]
