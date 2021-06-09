from . import views
from django.urls import path

app_name='ecommerce_app'

urlpatterns=[
    # path('',views.index,name='index'),
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdDetail, name='ProdCatDetail'),
]