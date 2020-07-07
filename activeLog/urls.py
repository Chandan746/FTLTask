
from django.urls import path
from . import views
urlpatterns = [
    path('sign_up/',views.sign_up,name="sign-up"),
    path('logout/',views.logout, name='blog_logout'),
    path('login/', views.login, name='blog_login'),
    path('',views.home,name = "home"),
    path('getjson/',views.gen_jason, name='getjson'),
]