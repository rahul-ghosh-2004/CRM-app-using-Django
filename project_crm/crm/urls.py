from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('update/<int:id>', views.update_cust_data_view, name='update_cust_data'),
]
