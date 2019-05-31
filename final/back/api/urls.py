from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('user_products/', views.UserProductList.as_view()),
    path('user_products/<int:pk>/', views.DeleteProduct.as_view()),
    path('login/',views.login),
    path('logout/',views.logout),
]
