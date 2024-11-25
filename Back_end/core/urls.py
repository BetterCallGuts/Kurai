from django.urls import path
from . import views
urlpatterns = [

    path(''       , views.index  , name='index'  ) ,
    path('cart/'  , views.cart   , name='cart'   ) ,
    path('detail/', views.detail , name='detail' ) ,

    path('auth/'  , views.auth   , name='auth'   ) ,
    path('store/' , views.store  , name='store'  ) ,    

    path('test/'  , views.test   , name='test'   ) ,
]