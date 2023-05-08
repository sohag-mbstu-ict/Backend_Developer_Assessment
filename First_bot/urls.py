from django.urls import path
from First_bot.views import GenericApiView_Product,GenericApiView_Product_Description
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.home, name="home"),
    path('generic_product/',GenericApiView_Product.as_view(),name="generic_product"),
    path('generic_product/<int:id>/',GenericApiView_Product.as_view(),name="generic_product"),
    path('generic_description/',GenericApiView_Product_Description.as_view(),name="generic_description"),
    path('generic_description/<int:id>/',GenericApiView_Product_Description.as_view(),name="generic_description"),
]