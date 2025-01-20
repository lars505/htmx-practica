from django.urls import path
from . import views, htmx_views

urlpatterns =[
    path('', views.all_products, name='products'),
] 
htmx_patterns = [
    path('check_product/', htmx_views.check_product, name='check_product'),
    path('validate_price/', htmx_views.validate_price, name="validate_price"),

    path('save_product/', htmx_views.save_product, name='save_product'),
    path('delete_product/<int:id_product>', htmx_views.delete_product, name='delete_product'),
]

urlpatterns += htmx_patterns