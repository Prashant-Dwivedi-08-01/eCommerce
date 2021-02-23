from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='ShopeHome'),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="Contact"),
    path('tracker/',views.tracker,name="TrackerUs"),
    path('search/',views.search,name="Search"),
    path('products/<int:myid>',views.productView,name="ProductView"),
    path('checkout/',views.checkout,name="CheckOut"),
    path('order/', views.order, name='Order')
]
