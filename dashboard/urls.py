from django.urls import path
from .import views

urlpatterns = [
    path("dashboard/", views.index, name = "dashboard_index"),
    path("staff/", views.staff, name = "dashboard_staff"),
    path("product/", views.product, name = "product"),
    path("product/delete<int:pk>/", views.product_delete, name = "product_delete"),
    path("product/update<int:pk>/", views.product_update, name = "product_update"),
    path("staff/staff_detail<int:pk>/", views.staff_detail, name = "staff_detail"),
    path("order/", views.order, name = "order"),

]